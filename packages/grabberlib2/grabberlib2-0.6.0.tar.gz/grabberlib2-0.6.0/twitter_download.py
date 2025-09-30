#!/usr/bin/env python3

import argparse
import http.cookiejar as cookiejar
import os
import re
import sys
import time
from pathlib import Path

import requests
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

# Optional dependency for cookie dumping
try:
    import browser_cookie3 as bc3
except ImportError:
    bc3 = None


# ===================== Cookie utilities =====================


def verify_x_cookies_file(cookies_path: str, timeout: float = 10.0) -> bool:
    """
    Best-effort check that cookies.txt represents a logged-in X session.
    Loads cookies and requests an account page that requires auth.
    Returns True if looks logged in, False otherwise.
    """
    cj = cookiejar.MozillaCookieJar()
    try:
        cj.load(cookies_path, ignore_discard=True, ignore_expires=True)
    except Exception as e:
        print(f"[error] Could not read cookies file: {e}", file=sys.stderr)
        return False

    domains = {c.domain for c in cj}
    if not any("x.com" in d or "twitter.com" in d for d in domains):
        print("[warn] cookies.txt has no x.com/twitter.com entries.", file=sys.stderr)

    s = requests.Session()
    s.cookies = cj
    s.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }
    )

    try:
        r = s.get("https://x.com/settings/account", allow_redirects=True, timeout=timeout)
    except requests.RequestException as e:
        print(f"[error] Network error while verifying cookies: {e}", file=sys.stderr)
        return False

    url_lower = r.url.lower()
    if any(k in url_lower for k in ["/login", "signin"]):
        print("[error] Cookies appear not logged in (redirected to login).", file=sys.stderr)
        return False
    if r.status_code in (401, 403):
        print(f"[error] Access denied with cookies (HTTP {r.status_code}).", file=sys.stderr)
        return False
    if r.status_code != 200:
        print(f"[warn] Unexpected status {r.status_code} at {r.url}. Cookies may be invalid.", file=sys.stderr)
        return False

    html = r.text
    looks_like_login = re.search(r"(?i)log in|sign in|password", html) and "settings" not in r.url
    if looks_like_login:
        print("[error] Page looks like a login form; cookies not accepted.", file=sys.stderr)
        return False

    print("[ok] cookies.txt looks valid for an authenticated X session.")
    return True


BROWSER_FUNCS = {
    "chrome": "chrome",
    "edge": "edge",
    "brave": "brave",
    "vivaldi": "vivaldi",
    "firefox": "firefox",
}


def dump_cookies_from_browser_to_file(browser: str, outpath: str) -> str:
    """
    Export cookies from the given browser's DEFAULT profile to a Netscape cookies.txt file.
    Only includes x.com / twitter.com cookies. Returns absolute path to the file.
    """
    if bc3 is None:
        raise RuntimeError("browser-cookie3 is not installed. Run: pip install browser-cookie3")

    bkey = (browser or "").lower()
    if bkey not in BROWSER_FUNCS:
        raise ValueError(f"Unsupported browser '{browser}'. Use one of: {', '.join(BROWSER_FUNCS)}")

    getter_name = BROWSER_FUNCS[bkey]
    getter = getattr(bc3, getter_name)

    # Pull per-domain cookies from the DEFAULT profile
    jar_x = getter(domain_name="x.com")
    jar_tw = getter(domain_name="twitter.com")

    for c in jar_tw:
        jar_x.set_cookie(c)

    out = Path(outpath).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# Generated at %s by download_x_video.py\n" % time.strftime("%Y-%m-%d %H:%M:%S"))
        f.write("# domain\tflag\tpath\tsecure\texpiration\tname\tvalue\n")
        for c in jar_x:
            if not (("x.com" in c.domain) or ("twitter.com" in c.domain)):
                continue
            domain = c.domain
            include_subdomains = "TRUE" if domain.startswith(".") else "FALSE"
            path = c.path or "/"
            secure = "TRUE" if getattr(c, "secure", False) else "FALSE"
            expires = int(getattr(c, "expires", 0) or 0)  # 0 for session cookies
            name = c.name
            value = c.value
            f.write(f"{domain}\t{include_subdomains}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n")

    return str(out)


# ===================== yt-dlp helpers =====================


def pick_best_format(formats: list[dict], prefer_mp4: bool = True) -> dict | None:
    """Pick the best *video* format, preferring MP4 container if requested."""
    if not formats:
        return None
    video_formats = [f for f in formats if f.get("vcodec") and f["vcodec"] != "none"]
    if not video_formats:
        return None

    def sort_key(f):
        return (f.get("height") or 0, f.get("tbr") or 0)

    best_overall = sorted(video_formats, key=sort_key)[-1]
    if prefer_mp4:
        mp4s = [f for f in video_formats if f.get("ext") == "mp4" or "mp4" in str(f.get("container", "")).lower()]
        if mp4s:
            return sorted(mp4s, key=sort_key)[-1]
    return best_overall


def collect_video_entries(info: dict) -> list[dict]:
    """
    Normalize yt-dlp output:
    - If single video: [info]
    - If playlist/collection: only items with real video streams
    - Skip photo-only items
    """
    out = []
    if not info:
        return out

    def has_video(entry: dict) -> bool:
        fmts = entry.get("formats") or []
        return any(f.get("vcodec") and f["vcodec"] != "none" for f in fmts)

    if isinstance(info.get("entries"), list):
        for it in info["entries"]:
            if has_video(it):
                out.append(it)
    else:
        if has_video(info):
            out.append(info)
    return out


def build_ydl_opts(
    *,
    base_opts: dict | None = None,
    outtmpl: str | None = None,
    format_selector: str | None = None,
    merge_to_mp4: bool = True,
    args: argparse.Namespace,
) -> dict:
    """
    One source of truth for yt-dlp options, including authentication.
    """
    opts = {
        "retries": 3,
        "quiet": True,
        "noprogress": True,
        "skip_download": True,  # overridden when downloading
    }
    if base_opts:
        opts.update(base_opts)

    # Authentication: cookies-from-browser (preferred) or cookies file
    if getattr(args, "cookies_from_browser", None):
        # Use ONLY the browser name (default profile). Do not include profile/keyring args.
        opts["cookiesfrombrowser"] = (args.cookies_from_browser,)
    elif getattr(args, "cookies", None):
        opts["cookiefile"] = args.cookies

    if outtmpl or format_selector:
        opts["skip_download"] = False
        opts["quiet"] = False
        opts["noprogress"] = False
        if outtmpl:
            opts["outtmpl"] = outtmpl
        if format_selector:
            opts["format"] = format_selector
        if merge_to_mp4:
            opts["merge_output_format"] = "mp4"

    return opts


def probe(url: str, args: argparse.Namespace) -> tuple[list[dict], dict]:
    """Extract metadata (authenticated if needed) without downloading."""
    ydl_opts = build_ydl_opts(args=args)
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return collect_video_entries(info), info


def download_video_entry(
    entry: dict,
    outdir: str,
    prefer_mp4: bool,
    format_id: str | None,
    args: argparse.Namespace,
) -> Path | None:
    """Download a single entry entry. We purposely avoid binding to a specific format_id
    because children in a playlist may expose different format_id values on re-extraction.
    Instead we pass a robust yt-dlp format selector expression so each item can pick its own best formats."""
    os.makedirs(outdir, exist_ok=True)

    # Build a robust format selector
    fmt_selector = format_id or ("bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b" if prefer_mp4 else "bv*+ba/b")

    base_title = (entry.get("title") or entry.get("id") or "x_video").strip()
    outtmpl = os.path.join(outdir, f"{base_title}-%(id)s.%(ext)s")

    ydl_opts = build_ydl_opts(
        args=args,
        outtmpl=outtmpl,
        format_selector=fmt_selector,
        merge_to_mp4=True,
    )

    target = entry.get("webpage_url") or entry.get("url")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([target])
    except DownloadError as exc:
        print(f"Download for {target} failed: {exc}")

    # Best-effort filename resolution (unchanged)
    try:
        with YoutubeDL(build_ydl_opts(args=args)) as ydl:
            after = ydl.extract_info(target, download=False)
        predict_title = (after.get("title") or after.get("id") or base_title).strip()
        candidates = [f for f in os.listdir(outdir) if f.startswith(predict_title) or f.startswith(base_title)]
        candidates.sort(key=lambda x: (not x.lower().endswith(".mp4"), -len(x)))
        if candidates:
            return Path(os.path.join(outdir, candidates[0]))
    except Exception:
        pass

    return None


# ===================== CLI =====================


def main():
    p = argparse.ArgumentParser(
        description="Download the video from an X/Twitter link, even if the post mixes photos + video."
    )
    p.add_argument("urls", nargs="+", help="X/Twitter post URL (x.com / twitter.com)")
    p.add_argument("-o", "--outdir", default="downloads", help="Output directory (default: downloads)")
    p.add_argument("--all", action="store_true", help="Download all videos if multiple are present")
    p.add_argument("--no-mp4-preference", action="store_true", help="Do not prefer MP4 when choosing best")
    p.add_argument("--format-id", default=None, help="Force a specific yt-dlp format_id (advanced)")

    # Auth options (simplified)
    p.add_argument(
        "--cookies-from-browser", help="Load cookies from the DEFAULT profile of: chrome, firefox, edge, brave, vivaldi"
    )
    p.add_argument("--cookies", help="Path to a Netscape-format cookies.txt (alternative to --cookies-from-browser)")

    # Cookie dump option
    p.add_argument(
        "--dump-cookies",
        metavar="FILE",
        help="Export default-profile browser cookies to a Netscape cookies.txt file, then exit.",
    )

    args = p.parse_args()

    # If user asked to DUMP cookies, do that and exit early
    if args.dump_cookies:
        if not args.cookies_from_browser:
            print("[error] --dump-cookies requires --cookies-from-browser <browser>", file=sys.stderr)
            sys.exit(2)
        try:
            out_file = dump_cookies_from_browser_to_file(args.cookies_from_browser, args.dump_cookies)
            print(f"[ok] Cookies saved to: {out_file}")
            print("Use later with:  --cookies", out_file)
            sys.exit(0)
        except Exception as e:
            print(f"[error] Failed to dump cookies: {e}", file=sys.stderr)
            sys.exit(1)

    # If using a cookies file, verify it first (best-effort)
    if args.cookies:
        if not verify_x_cookies_file(args.cookies):
            print(
                "[hint] Re-export cookies while logged into x.com, or use --cookies-from-browser instead.",
                file=sys.stderr,
            )
            sys.exit(1)

    # From here on, we expect a URL
    if not args.urls:
        p.error("the following arguments are required: url (unless using --dump-cookies)")

    videos_entries_to_download = []
    video_entries = None
    raw = None
    for url in args.urls:
        try:
            video_entries, raw = probe(url, args)
            videos_entries_to_download.append((video_entries, raw))
        except DownloadError as e:
            print(f"[error] Failed to extract info: {e}", file=sys.stderr)
            print(
                "[hint] If this is sensitive/age-gated or protected media, pass "
                "--cookies-from-browser <your_browser> or --cookies <cookies.txt>",
                file=sys.stderr,
            )
            continue
        except Exception as e:
            print(f"[error] Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)

    if not videos_entries_to_download or not (video_entries and raw):
        if raw and raw.get("thumbnails"):
            print("[info] No video found. This link appears to contain only photos.")
        else:
            print(
                "[info] No downloadable video detected. The post may be photos-only, private, deleted, restricted, or region-locked."
            )
        sys.exit(2)

    if len(videos_entries_to_download) > 1 and not args.all:
        print(f"[info] Found {len(video_entries)} video items. Downloading the first one.")
        print("       (Use --all to download each video.)")

    prefer_mp4 = not args.no_mp4_preference
    # bot = Bot(token=f"{BOT_TOKEN}")
    # channel = "@myprovideos"

    for video_entries, raw in videos_entries_to_download:
        to_download = video_entries if args.all else [video_entries[0]]
        for idx, entry in enumerate(to_download, 1):
            label = f"{idx}/{len(to_download)}" if len(to_download) > 1 else "1/1"
            print(f"[info] Downloading video {label} …")
            outpath = download_video_entry(
                entry,
                args.outdir,
                prefer_mp4=prefer_mp4,
                format_id=args.format_id,
                args=args,
            )
            # if outpath:
            #     post_text = outpath.name
            #     builder = MediaGroupBuilder(caption=post_text)
            #     video = FSInputFile(path=outpath.as_posix(), filename=outpath.name)
            #     builder.add_video(media=video)
            #     _ = asyncio.run(bot.send_media_group(chat_id=channel, media=builder.build()))
            if outpath:
                print(f"[ok] Saved: {outpath}")
            else:
                print("[warn] Download completed but exact filename could not be resolved.")

    sys.exit(0)


if __name__ == "__main__":
    main()
