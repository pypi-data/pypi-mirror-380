# Previous code for image downloading
import asyncio
import aiofiles
import aiohttp
import pathlib
import re
from collections.abc import Coroutine, Iterable
from typing import Any, TypeVar

import httpx
from boltons.setutils import IndexedSet
from bs4 import BeautifulSoup
from PIL import Image
from tqdm import tqdm

from grabber.core.settings import get_media_root

from .api import get_images_reponse_with_aiohttp
from .constants import DEFAULT_PER_IMAGE_CONCURRENCY, headers_mapping

T = TypeVar("T")


def wrapper(coro: Coroutine[Any, Any, T]) -> T:
    return asyncio.run(coro)


async def convert_from_webp_to_jpg(folder: pathlib.Path) -> None:
    files = list(folder.iterdir())
    tqdm_iterable = tqdm(
        files,
        total=len(files),
        desc="Converting images from WebP to JPEG",
        leave=False,
    )

    for file in tqdm_iterable:
        if file.suffix == ".webp":
            image = Image.open(file).convert("RGB")
            new_file = file.with_suffix(".jpg")
            image.save(new_file, "JPEG")
            file.unlink()


async def downloader(
    titles: list[str],
    title_folder_mapping: dict[str, tuple[Iterable[IndexedSet], pathlib.Path]],
    headers: dict[str, str] | None = None,
    per_image_concurrency: int = DEFAULT_PER_IMAGE_CONCURRENCY,
) -> None:
    """
    Kick off downloads for multiple titles in parallel (one task per title).
    Each title downloads its images concurrently (bounded by per_image_concurrency).
    """
    tasks = [
        download_images(
            images_set=title_folder_mapping[title][0],
            new_folder=title_folder_mapping[title][1],
            title=title,
            headers=headers,
            per_image_concurrency=per_image_concurrency,
        )
        for title in titles
    ]
    # Run all titles concurrently
    await asyncio.gather(*tasks)


async def download_images(
    images_set: Iterable[IndexedSet],
    new_folder: pathlib.Path,
    title: str,
    headers: dict[str, str] | None = None,
    per_image_concurrency: int = DEFAULT_PER_IMAGE_CONCURRENCY,
) -> str:
    """
    Download all images for a single title concurrently (bounded).
    images_set should be an iterable of tuples: (index, filename, url)
    """
    new_folder.mkdir(parents=True, exist_ok=True)

    sem = asyncio.Semaphore(per_image_concurrency)
    images_list = list(images_set)  # ensure we can len() and iterate twice
    total = len(images_list)
    pbar = tqdm(total=total, desc=f"Downloading images for {title} in {new_folder}")

    # If you pass headers here, requests will inherit them by default.
    timeout = aiohttp.ClientTimeout(total=None, sock_connect=30, sock_read=300)
    async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:

        async def fetch_one(_idx: int, img_filename: str, image_url: str) -> pathlib.Path:
            path = new_folder / img_filename
            async with sem:
                # Retry the whole request+read via get_image_stream
                image_content = await get_images_reponse_with_aiohttp(session, image_url, headers=None)
                # Write atomically-ish
                async with aiofiles.open(path, 'wb') as file:
                    await file.write(image_content)
                pbar.set_description(f"Saved image {path}")
                pbar.update(1)
                return path

        # Kick off all downloads
        results = await asyncio.gather(*(fetch_one(*t) for t in images_list))

    pbar.close()

    # Convert after all downloads if any .webp present
    if any(p.suffix.lower() == ".webp" for p in results):
        await convert_from_webp_to_jpg(new_folder)

    return "Done"


async def download_from_bunkr(
    links: list[str],
    headers: dict[str, str] | None = None,
) -> None:
    if headers is None:
        headers = headers_mapping["bunkr"]

    query = "div.grid-images div.grid-images_box div a.grid-images_box-link"

    for link in links:
        sources = set()
        soup = BeautifulSoup(httpx.get(link, headers=headers).content)
        a_tags = soup.select(query)
        for a_tag in a_tags:
            sources.add(a_tag.attrs["href"])

        for source in sources:
            second_soup = BeautifulSoup(httpx.get(source, headers=headers).content)
            video_source = second_soup.find("source")
            video_url = video_source.attrs["src"]
            filename = video_url.rsplit("/", 2)[-1]
            video_resp = httpx.get(video_url, headers=headers, stream=True)
            with open(get_media_root() / filename, "wb") as file:
                for chunk in video_resp.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        file.flush()


async def run_downloader(
    final_dest: pathlib.Path | str,
    page_title: str,
    unique_img_urls: IndexedSet,
    titles: IndexedSet,
    title_folder_mapping: dict[str, tuple[IndexedSet, pathlib.Path]],
    headers: dict[str, str] | None = None,
) -> None:
    await downloader(
        titles=list(titles),
        title_folder_mapping=title_folder_mapping,
        headers=headers,
    )


async def upload_to_r2_and_post_to_telegram(
    folder: pathlib.Path,
) -> None:
    pass


def generate_hashtags(text: str) -> str:
    # Split into parts (separates words and emojis)
    parts = text.split()

    # Separate words (alphanumeric + underscore) from emojis/symbols
    words = [part for part in parts if re.match(r"^[a-zA-Z0-9_]+$", part)]
    non_words = [part for part in parts if not re.match(r"^[a-zA-Z0-9_]+$", part)]

    if not words:
        return ""

    # First hashtag: ALL words before emojis (if any) combined
    # If there are non-words (emojis), split into before & after emoji
    if non_words:
        # Find where the first emoji appears
        first_emoji_pos = parts.index(non_words[0])
        words_before_emoji = [p for p in parts[:first_emoji_pos] if re.match(r"^[a-zA-Z0-9_]+$", p)]
        hashtag1 = "".join(words_before_emoji)
    else:
        hashtag1 = "".join(words)  # No emojis, combine all

    # Second hashtag: Last word (if different)
    hashtag2 = words[-1] if (len(words) > 1 and words[-1].lower() != hashtag1.lower()) else None

    # Generate result
    result = f"#{hashtag1}"
    if hashtag2:
        result += f" #{hashtag2}"

    return result






























import asyncio
from grabber.core.utils import get_new_telegraph_client
from grabber.core.bot.core import send_message
from telegraph import TelegraphException, exceptions
from time import sleep


def upload_file(file, retry_count=5, telegraph=None):
    try:
        print(f"Trying to upload {file.name}")
        resp = telegraph.upload_file(file)
    except (TelegraphException, exceptions.RetryAfterError) as exc:
        print(f"Error trying to upload {file.name}: {exc}")
        if retry_count in [10, 15, 20, 25] or retry_count > 25:
            print("Creating new account for new token")
            account = telegraph.create_account(
                short_name=SHORT_NAME,
                author_name=AUTHOR_NAME,
                author_url=AUTHOR_URL,
                replace_token=True,
            )
            telegraph = Telegraph(access_token=account["access_token"])
        print(f"Sleeping {retry_count} before trying to upload again")
        sleep(retry_count)
        retry_count += 1
        resp = upload_file(file, retry_count=retry_count, telegraph=telegraph)
    if not resp:
        resp = upload_file(file, retry_count=retry_count, telegraph=telegraph)
    print(f"Uploaded {file.name}! URL: {resp[0]['src']}")
    file_resp = resp[0]
    return file_resp["src"]


def upload_files(files, retry_count=5, telegraph=None):
    urls = set()
    for file in files:
        urls.add(upload_file(file=file, retry_count=retry_count, telegraph=telegraph))
    return urls


def create_page(
    title: str,
    html_content: str,
    telegraph_client,
    try_again=True,
) -> str:
    try:
        page = telegraph_client.create_page(title=title, html_content=html_content)
    except (
        Exception,
        exceptions.TelegraphException,
        exceptions.RetryAfterError,
    ) as exc:
        error_message = str(exc)
        if "try again" in error_message.lower() or "retry" in error_message.lower():
            sleep(5)
            if try_again:
                telegraph_client = get_new_telegraph_client()
                return create_page(
                    title=title,
                    html_content=html_content,
                    telegraph_client=telegraph_client,
                    try_again=False,
                )
    return page["url"]


def create_new_page(title, urls, telegraph_client) -> str:
    html_template = """<figure contenteditable="false"><img src="{file_path}"><figcaption dir="auto" class="editable_text" data-placeholder="{title}"></figcaption></figure>"""
    contents = []

    for url in urls:
        contents.append(html_template.format(file_path=url, title=title))

    content = "\n".join(contents)
    page_url = create_page(
        title=title,
        html_content=content,
        telegraph_client=telegraph_client,
    )

    post = f"{title} - {page_url}"
    asyncio.run(send_message(post))

    return post



import pathlib
import shutil
from typing import Any
import asyncio
import multiprocessing
import pathlib
import shutil
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import sleep
from typing import Any

import requests
from tenacity import retry, wait_chain, wait_fixed
from tqdm import tqdm
from boltons.setutils import IndexedSet

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()

def wrapper(coro):
    return asyncio.run(coro)


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}


@retry(
    wait=wait_chain(
        *[wait_fixed(3) for _ in range(5)]
        + [wait_fixed(7) for _ in range(4)]
        + [wait_fixed(9) for _ in range(3)]
        + [wait_fixed(15)],
    ),
    reraise=True,
)
def get_image_stream(
    url,
    headers: dict[str, Any] = None,
) -> requests.Response:
    """Wait 3s for 5 attempts
    7s for the next 4 attempts
    9s for the next 3 attempts
    then 15 for all attempts thereafter
    """
    if headers is not None:
        r = requests.get(url, headers=headers, stream=True)
    else:
        r = requests.get(url, stream=True)

    if r.status_code >= 300:
        raise Exception(f"Not able to retrieve {url}: {r.status_code}\n")

    return r


def download_images(
    images_set,
    new_folder: pathlib.Path,
    title: str,
    headers: dict[str, str] = None,
) -> str:
    """Download an image from a given URL and save it to the specified filename.

    Parameters
    ----------
    - image_url: The URL of the image to be downloaded.
    - filename: The filename to save the image to.

    """
    result = {}
    tqdm_iterable = tqdm(
        images_set,
        total=len(images_set),
        desc=f"Downloading images for {title} in {new_folder}",
    )
    folder_files = list(new_folder.iterdir())

    for image_url in tqdm_iterable:
        img_filename = image_url.split("/")[-1]
        filename = new_folder / f"{img_filename}"
        if filename not in folder_files:
            resp = get_image_stream(image_url, headers=headers)

            with open(filename.as_posix(), "wb") as img_file:
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, img_file)
            tqdm_iterable.set_description(f"Saved image {filename}")


    result[title] = new_folder

    return "Done"


async def downloader(
    titles: list[str],
    title_folder_mapping: dict[str, tuple[IndexedSet, pathlib.Path]],
    headers: dict[str, str] | None = None,
) -> None:
    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_NUMBER) as executor:
        # Dictionary to hold Future objects
        futures_to_title = {}
        future_counter = 0
        coroutines = []
        for title in titles:
            images_set, folder_dest = title_folder_mapping[title]
            partial_download = partial(
                download_images,
                images_set=images_set,
                new_folder=folder_dest,
                headers=headers,
                title=title,
            )
            coroutines.append(partial_download())
            future_counter += 1

        # Handling futures as they complete
        for future in tqdm(
            executor.map(wrapper, coroutines),
            total=future_counter,
            desc=f"Retrieving {future_counter} tasks of downloading images",
        ):
            print(future)  # Get the result from the future object


images = set()
url = "https://leakxxx.com/api/v1/user/rintohsaka?page={page}&types[]=image&types[]=video&types[]=gallery&nsfw[]=0"

for page in tqdm(range(1, 30)):
    r = httpx.get(url.format(page=page))

    if r.status_code == 200:
        for post in r.json()["data"]["posts"]:
            image_url = post["data"]["url"]
            images.add(image_url)
    else:
        print(f"There was no response for page {page}")

print(len(images))
download_images(images, new_folder, title, headers=headers)
