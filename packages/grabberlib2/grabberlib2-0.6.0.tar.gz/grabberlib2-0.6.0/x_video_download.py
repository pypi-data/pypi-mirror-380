#!/usr/bin/env python3
"""
x_video_download.py

Download a video from an X (Twitter) post using the v2 API with media.variants.
- Requires: tweepy, requests
- Auth: bearer token with read access (app-only is fine for public posts)
  * Set environment variable X_BEARER_TOKEN, or pass --bearer on the CLI.

Usage:
    python x_video_download.py https://x.com/user/status/1770000000000000000
    python x_video_download.py 1770000000000000000 --output myclip.mp4
    python x_video_download.py 1770000000000000000 --bearer <token>

Notes:
- Picks the highest bitrate "video/mp4" variant. If only HLS is available, use --allow-hls
  to output the m3u8 URL to a .txt file (or handle it with ffmpeg/yt-dlp).
- Respects creator rights and X's Terms.
"""

import argparse
import os
import re
import sys

import requests
import tweepy


def extract_tweet_id(url_or_id: str) -> str:
    """
    Accepts either a numeric ID or a full x.com/twitter.com URL and returns the numeric ID.
    """
    s = url_or_id.strip()
    # If it's just digits, assume it's the ID
    if s.isdigit():
        return s

    # Regex to capture the numeric status ID from URL
    m = re.search(r"/status/(\d+)", s)
    if m:
        return m.group(1)

    raise ValueError(f"Could not extract a tweet ID from: {url_or_id}")


def pick_best_mp4_variant(variants: list[dict]) -> dict | None:
    """
    Among v2 media.variants, choose the highest bit_rate 'video/mp4' entry.
    """
    mp4s = [v for v in variants if v.get("content_type") == "video/mp4" and "url" in v]
    if not mp4s:
        return None
    return sorted(mp4s, key=lambda v: v.get("bit_rate", 0), reverse=True)[0]


def fetch_video_variants(client: tweepy.Client, tweet_id: str) -> tuple[dict | None, str | None]:
    """
    Fetch media variants for a tweet ID using v2 endpoints.
    Returns (best_mp4_variant, hls_url) where either may be None.
    """
    resp = client.get_tweets(
        ids=[tweet_id],
        expansions=["attachments.media_keys"],
        media_fields=["variants", "type", "duration_ms", "preview_image_url"],
    )

    if not resp or not resp.data:
        raise RuntimeError("Tweet not found or inaccessible. Is it deleted/private?")

    includes = getattr(resp, "includes", None) or {}
    media_items = includes.get("media", [])

    videos = [m for m in media_items if getattr(m, "type", None) in ("video", "animated_gif")]
    if not videos:
        raise RuntimeError("No video found on this post.")

    # Collect variants across all media (in case of multiple videos)
    all_variants = []
    for m in videos:
        vars_ = getattr(m, "variants", None) or []
        all_variants.extend(vars_)

    best_mp4 = pick_best_mp4_variant(all_variants)
    hls = next((v.get("url") for v in all_variants if v.get("content_type") == "application/x-mpegURL"), None)

    return best_mp4, hls


def stream_download(url: str, out_path: str) -> None:
    """
    Stream the MP4 to disk.
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length") or 0)
        chunk = 1024 * 256
        downloaded = 0
        with open(out_path, "wb") as f:
            for part in r.iter_content(chunk_size=chunk):
                if not part:
                    continue
                f.write(part)
                downloaded += len(part)
                if total:
                    pct = int(downloaded * 100 / total)
                    sys.stdout.write(f"\rDownloading: {pct}% ({downloaded}/{total} bytes)")
                    sys.stdout.flush()
        if total:
            sys.stdout.write("\n")
    print(f"Saved: {out_path}")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Download X/Twitter video via API v2 media.variants")
    p.add_argument("url_or_id", help="Tweet URL or numeric ID")
    p.add_argument("--bearer", help="X API v2 bearer token (defaults to env X_BEARER_TOKEN)")
    p.add_argument("--output", "-o", help="Output filename (default: <tweet_id>.mp4)")
    p.add_argument(
        "--allow-hls",
        action="store_true",
        help="If no MP4 is available, write the HLS .m3u8 URL to <tweet_id>.m3u8.txt",
    )
    args = p.parse_args(argv)

    bearer = args.bearer or os.getenv("X_BEARER_TOKEN")
    if not bearer:
        print("Error: missing bearer token. Set X_BEARER_TOKEN or pass --bearer.", file=sys.stderr)
        return 2

    try:
        tweet_id = extract_tweet_id(args.url_or_id)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    client = tweepy.Client(bearer_token=bearer, wait_on_rate_limit=True)

    try:
        best_mp4, hls_url = fetch_video_variants(client, tweet_id)
    except tweepy.TweepyException as e:
        print(f"Twitter/X API error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if best_mp4:
        url = best_mp4["url"]
        out = args.output or f"{tweet_id}.mp4"
        stream_download(url, out)
        return 0

    if hls_url and args.allow_hls:
        txt_path = args.output or f"{tweet_id}.m3u8.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(hls_url + "\n")
        print(f"No MP4 variant. Wrote HLS URL to: {txt_path}")
        return 0

    print("No MP4 variant available. Re-run with --allow-hls to capture the HLS URL.", file=sys.stderr)
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
