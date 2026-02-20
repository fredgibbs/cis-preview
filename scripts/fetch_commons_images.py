#!/usr/bin/env python3
"""
Fetch Creative Commons images from Wikimedia Commons for ScrollStories.

- Reads a YAML manifest describing desired images (search queries or direct URLs)
- Downloads images into each story's images/ folder
- Writes/updates a simple attributions.txt next to downloaded files

Usage:
  python scripts/fetch_commons_images.py --manifest scrollstories/nacho_investigation/images/manifest.yml
  python scripts/fetch_commons_images.py --all  # scans for any manifest.yml under scrollstories/*/images

Requirements:
  pip install requests pyyaml
"""
import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlencode

import requests
import yaml

WIKIMEDIA_API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "class-project-template-image-fetcher/1.0 (education use)"}


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def sanitize_filename(name: str) -> str:
    name = re.sub(r"[^A-Za-z0-9_.-]", "_", name)
    return name[:128]


def commons_search(query: str, limit: int = 10):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,  # File namespace on Commons
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|user|size",
        "iiurlwidth": 1200,
        "origin": "*",
    }
    r = requests.get(WIKIMEDIA_API, params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    pages = data.get("query", {}).get("pages", {})
    results = []
    for _, page in pages.items():
        info = page.get("imageinfo", [{}])[0]
        if not info:
            # Not a file page or missing imageinfo
            continue
        thumb = info.get("thumburl") or info.get("url")
        meta = info.get("extmetadata", {})
        author = meta.get("Artist", {}).get("value") or meta.get("Credit", {}).get("value")
        license_short = meta.get("LicenseShortName", {}).get("value")
        desc = meta.get("ImageDescription", {}).get("value")
        results.append({
            "title": page.get("title"),
            "url": info.get("url"),
            "thumb": thumb,
            "author": author,
            "license": license_short,
            "description": desc,
        })
    return results


def download(url: str, dest: Path):
    with requests.get(url, stream=True, headers=HEADERS, timeout=60) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


def download_with_retry(url: str, dest: Path, retries: int = 1):
    for attempt in range(retries + 1):
        try:
            download(url, dest)
            return True
        except requests.HTTPError as e:
            status = getattr(e.response, "status_code", None)
            if status == 429 and attempt < retries:
                time.sleep(3.0 * (attempt + 1))
                continue
            print(f"Skip download after {attempt+1} attempts ({status}): {url}")
            return False


def write_attrib(dest_dir: Path, entries):
    attrib = dest_dir / "attributions.txt"
    lines = []
    for e in entries:
        line = f"{e['filename']} — {e.get('author','Unknown')} — {e.get('license','')} — {e.get('title','')}\n"
        lines.append(line)
    with open(attrib, "a", encoding="utf-8") as f:
        f.writelines(lines)


def process_manifest(manifest_path: Path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        m = yaml.safe_load(f) or {}
    out_dir = manifest_path.parent
    ensure_dir(out_dir)

    downloaded = []

    items = m.get("images", [])
    default_limit = int(m.get("default_limit", 3))

    for item in items:
        if "url" in item:
            url = item["url"]
            filename = sanitize_filename(item.get("filename") or Path(url).name)
            dest = out_dir / filename
            ok = True
            if not dest.exists():
                ok = download_with_retry(url, dest, retries=2)
            if ok:
                downloaded.append({"filename": filename, "author": item.get("author"), "license": item.get("license"), "title": item.get("title")})
        elif "query" in item:
            limit = int(item.get("limit", default_limit))
            results = commons_search(item["query"], limit=limit)
            for i, res in enumerate(results, start=1):
                filename = sanitize_filename(item.get("prefix", "img") + f"_{i}.jpg")
                dest = out_dir / filename
                # Prefer thumbnail URL to reduce bandwidth; fall back to original
                dl_url = res.get("thumb") or res.get("url")
                ok = True
                if not dest.exists() and dl_url:
                    ok = download_with_retry(dl_url, dest, retries=2)
                if ok:
                    downloaded.append({"filename": filename, "author": res.get("author"), "license": res.get("license"), "title": res.get("title")})
                time.sleep(1.5)
        else:
            print(f"Skip entry without url or query: {item}")

    if downloaded:
        write_attrib(out_dir, downloaded)
        print(f"Saved {len(downloaded)} images to {out_dir}")
    else:
        print(f"No images downloaded for {manifest_path}")


def find_all_manifests(base: Path):
    manifests = []
    manifests += list(base.glob("scrollstories/*/images/manifest.yml"))
    manifests += list(base.glob("essays/**/images/manifest.yml"))
    return manifests


def main():
    parser = argparse.ArgumentParser(description="Fetch Wikimedia Commons images per manifest.yml")
    parser.add_argument("--manifest", type=str, help="Path to a specific manifest.yml")
    parser.add_argument("--all", action="store_true", help="Scan all scrollstories/*/images/manifest.yml")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]

    manifests = []
    if args.manifest:
        manifests = [Path(args.manifest)]
    elif args.all:
        manifests = find_all_manifests(repo_root)
    else:
        print("Specify --manifest <path> or --all")
        sys.exit(1)

    for m in manifests:
        if not m.exists():
            print(f"Manifest not found: {m}")
            continue
        process_manifest(m)


if __name__ == "__main__":
    main()
