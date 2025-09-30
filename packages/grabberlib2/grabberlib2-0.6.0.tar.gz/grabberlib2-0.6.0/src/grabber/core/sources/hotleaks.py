import asyncio
import pathlib
from typing import Any

import httpx
from boltons.setutils import IndexedSet
from telegraph import Telegraph
from tenacity import retry, wait_chain, wait_fixed
from tqdm import tqdm
from unidecode import unidecode
from url_parser import parse_url

from grabber.core.utils import (
    get_soup,
    headers_mapping,
    run_downloader,
    send_post_to_telegram,
)


@retry(
    wait=wait_chain(
        *[wait_fixed(3) for _ in range(5)]
        + [wait_fixed(7) for _ in range(4)]
        + [wait_fixed(9) for _ in range(3)]
        + [wait_fixed(15)],
    ),
    reraise=True,
)
async def get_response(url: str, headers: dict[str, str]) -> httpx.Response:
    error_response = {"message": "Server Error"}
    try:
        response = httpx.get(url=url, headers=headers)
        response.raise_for_status()

        for data in response.json():
            if "message" in data and data["message"] == error_response["message"]:
                raise httpx.HTTPStatusError(
                    f"Error response received from {url}: {data['message']}",
                    request=response.request,
                    response=response,
                )
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred for {url}: {exc}")
        raise
    except httpx.RequestError as exc:
        print(f"Request error occurred for {url}: {exc}")
        raise
    return response


async def get_pages_from_pagination(
    url: str,
    headers: dict[str, str],
) -> IndexedSet:
    referer_header = {"Referer": url}
    headers.update(referer_header)
    parsed_url: dict[str, str] = parse_url(url)
    model_name: str = parsed_url["dir"].replace("/", "")
    base_url = "https://hotleaks.tv/{model_name}?page={page_number}&type=photos&order=0"
    page_number = 1
    endpoint = base_url.format(model_name=model_name, page_number=page_number)
    response = httpx.get(url=endpoint, headers=headers)
    response_data: list[dict[str, Any]] = response.json()
    images_tags = IndexedSet()

    while response_data:
        for idx, data in enumerate(response_data):
            image_url = data["player"]
            parsed_image_url = parse_url(image_url)
            image_prefix = f"{idx + 1}".zfill(4)
            image_filename = parsed_image_url["file"]

            images_tags.add((image_prefix, f"{image_prefix}-{image_filename}", f"{image_filename}", image_url))

        page_number += 1
        next_page_url = base_url.format(model_name=model_name, page_number=page_number)
        await asyncio.sleep(0.5)  # To avoid hitting the server too hard
        try:
            response = await get_response(url=next_page_url, headers=headers)
        except (Exception, httpx.HTTPStatusError, httpx.RequestError) as exc:
            print(f"Error when requesting {next_page_url}: {exc}")
            continue
        response_data = response.json()

    ordered_unique_img_urls = IndexedSet(sorted(images_tags, key=lambda x: list(x).pop(0)))
    ordered_unique_img_urls = IndexedSet([a[1:] for a in ordered_unique_img_urls])

    return ordered_unique_img_urls


async def get_sources_for_hotleaks(
    sources: list[str],
    entity: str,
    telegraph_client: Telegraph | None = None,
    final_dest: str | pathlib.Path = "",
    save_to_telegraph: bool | None = False,
    **kwargs: Any,
) -> None:
    tqdm_sources_iterable = tqdm(
        sources,
        total=len(sources),
        desc="Retrieving URLs...",
    )
    headers = headers_mapping[entity] if entity in headers_mapping else headers_mapping["common"]
    page_title = ""
    title_folder_mapping = {}
    posts_sent_counter = 0
    titles = IndexedSet()
    ordered_unique_img_urls = None
    ordered_unique_video_urls = None
    all_sources: list[str] = []
    original_folder_path = final_dest
    channel = kwargs.get("channel", "")

    for source_url in tqdm_sources_iterable:
        final_dest = pathlib.Path(str(original_folder_path)) if final_dest else ""
        all_sources.append(source_url)
        soup = await get_soup(
            target_url=source_url,
        )

        ordered_unique_img_urls = await get_pages_from_pagination(
            url=source_url,
            headers=headers,
        )

        title_tag = soup.find("title")
        if not title_tag:
            page_title_tag = soup.select("div.actor-name")
            if page_title_tag:
                page_title = page_title_tag[0]
                page_title = page_title.get_text().split("Hotleaks.tv")[0].split("on")[0].replace("https:", "")
            else:
                page_title = parse_url(source_url)["dir"].replace("/", "")
        else:
            page_title = title_tag.get_text(strip=True).split("Hotleaks.tv")[0].split("on")[0].replace("https:", "")

        page_title = page_title.split("[")[0].strip()
        page_title = unidecode(
            " ".join(
                f"#{part.strip().replace(' ', '').replace('.', '_').replace('-', '_')}"
                for part in page_title.split("/")
            )
        )
        titles.add(page_title)

        if final_dest:
            final_dest = pathlib.Path(final_dest) / unidecode(f"{page_title} - {entity}")
            if not final_dest.exists():
                final_dest.mkdir(parents=True, exist_ok=True)

            title_folder_mapping[page_title] = (ordered_unique_img_urls, final_dest)

        if save_to_telegraph:
            _ = await send_post_to_telegram(
                ordered_unique_img_urls=ordered_unique_img_urls,
                ordered_unique_video_urls=ordered_unique_video_urls,
                page_title=page_title,
                telegraph_client=telegraph_client,
                posts_sent_counter=posts_sent_counter,
                tqdm_sources_iterable=tqdm_sources_iterable,
                all_sources=all_sources,
                source_url=source_url,
                entity=entity,
                channel=channel,
            )
            page_title = ""

    if final_dest and ordered_unique_img_urls:
        await run_downloader(
            final_dest=final_dest,
            page_title=page_title,
            unique_img_urls=ordered_unique_img_urls,
            titles=titles,
            title_folder_mapping=title_folder_mapping,
            headers=headers,
        )
