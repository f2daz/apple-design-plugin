#!/usr/bin/env python3
"""Catalog, download and install Apple Design Resources.

    python3 resources.py list [--platform ios] [--kind font|figma|sketch|dmg|...] [--json]
    python3 resources.py show <query>                 # all links of matching resources
    python3 resources.py sync                         # re-read developer.apple.com/design/resources
    python3 resources.py download <query|preset|all> [--accept-license]
                          presets: fonts, essentials, bezels-iphone, bezels-ipad, bezels-mac,
                                   bezels-watch, glyphs
    python3 resources.py install-fonts [SF-Pro SF-Compact SF-Mono NY …] --accept-license
    python3 resources.py status                       # what is downloaded / installed

Downloads land in $APPLE_DESIGN_HOME/downloads (default ~/.apple-design/downloads).
Apple's resources are licensed, not redistributable: they are fetched from Apple on your machine,
and fonts may only be used to design and develop software for Apple platforms (see the licence in
each DMG). Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

PAGE = "https://developer.apple.com/design/resources/"
UA = "apple-design-plugin/1.0"
BUNDLED = Path(__file__).resolve().parent.parent / "data" / "resources.json"
FONT_DMGS = ["SF-Pro", "SF-Compact", "SF-Mono", "NY"]
# Named bundles for `download`, focused on iOS, iPadOS, macOS and watchOS
PRESETS = {
    "fonts": ["SF-Pro.dmg", "SF-Compact.dmg", "SF-Mono.dmg", "NY.dmg"],
    "essentials": ["SF-Pro.dmg", "SF-Compact.dmg", "SF-Mono.dmg", "NY.dmg", "SF-Symbols-",
                   "Icon-Templates"],
    "bezels-iphone": ["Bezel-iPhone-"],
    "bezels-ipad": ["Bezel-iPad-"],
    "bezels-mac": ["Bezel-MacBook-", "Bezel-iMac-", "Bezel-Studio-Displays"],
    "bezels-watch": ["Bezel-Apple-Watch-"],
    "glyphs": ["Glyph-", "Icon-", "Logo-"],
}
LICENSE_NOTE = (
    "Apple license: the fonts may only be used for mock-ups/development of software for Apple "
    "platforms; templates/bezels are subject to the Apple Design Resources license. "
    "Passing --accept-license confirms that you have read the license inside the DMG."
)


def home() -> Path:
    return Path(os.environ.get("APPLE_DESIGN_HOME", Path.home() / ".apple-design"))


def http_get(url: str) -> bytes:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read()
    except urllib.error.URLError as e:
        if "CERTIFICATE_VERIFY_FAILED" not in str(e) or not shutil.which("curl"):
            raise
    return subprocess.run(["curl", "-sSfL", "-A", UA, url], capture_output=True, check=True).stdout


# --------------------------------------------------------------------------- catalog

def kind_of(url: str) -> str:
    u = url.lower()
    if "figma.com" in u:
        return "figma"
    if "sketch.com" in u or u.startswith("sketch://"):
        return "sketch"
    if u.split("?")[0].endswith(".dmg"):
        return "dmg"
    if "/download/" in u or "apps.apple.com" in u:
        return "app"
    return "web"


def text(s: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def parse_links(chunk: str) -> list[dict]:
    links = []
    for a in re.finditer(r'<a href="([^"]+)"[^>]*>(.*?)</a>(?:\s*<p[^>]*>(.*?)</p>)?', chunk, re.S):
        url = html.unescape(a.group(1))
        if url.startswith("/"):
            url = "https://developer.apple.com" + url
        links.append({"label": text(a.group(2)), "url": url, "kind": kind_of(url),
                      "note": text(a.group(3) or "")})
    return links


def parse_page(page: str) -> list[dict]:
    """Split the resources page into <section> blocks and their grid items."""
    items = []
    main = page[page.find("<main"):page.find("</main>")]
    for sec in re.finditer(r'<section([^>]*)>(.*?)</section>', main, re.S):
        sec_id = (re.search(r'id="([^"]+)"', sec.group(1)) or [None, ""])[1]
        body = sec.group(2)
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", body, re.S)
        if not h2:
            continue
        section = text(h2.group(1))
        sec_id = sec_id or re.sub(r"[^a-z0-9]+", "-", section.lower()).strip("-")
        found = 0
        for cell in re.split(r'<div class="grid-item', body)[1:]:
            title = re.search(r"<h[3-5][^>]*>(.*?)</h[3-5]>", cell, re.S)
            links = parse_links(cell)
            if not title or not links:
                continue
            desc = re.search(r'<p class="[^"]*(?:description|copy)[^"]*"[^>]*>(.*?)</p>', cell, re.S)
            items.append({"section": section, "section_id": sec_id, "title": text(title.group(1)),
                          "description": text(desc.group(1)) if desc else "", "links": links})
            found += 1
        if not found:  # tool sections (SF Symbols, Icon Composer, Badges) have no item grid
            intro = re.search(r"<p[^>]*>(.*?)</p>", body, re.S)
            links = parse_links(body)
            if links:
                items.append({"section": section, "section_id": sec_id, "title": section,
                              "description": text(intro.group(1)) if intro else "", "links": links})
    return items


def platforms_for(item: dict) -> list[str]:
    s = f"{item['section']} {item['title']}".lower()
    found = [p for p in ("ios", "ipados", "macos", "watchos", "tvos", "visionos") if p in s]
    if "watch" in s and "watchos" not in found:
        found.append("watchos")
    if any(k in s for k in ("iphone",)):
        found.append("ios")
    if "ipad" in s and "ipados" not in found:
        found.append("ipados")
    if any(k in s for k in ("mac", "imac", "studio display")) and "macos" not in found:
        found.append("macos")
    return sorted(set(found)) or ["all"]


def sync() -> Path:
    page = http_get(PAGE).decode("utf-8", errors="replace")
    items = parse_page(page)
    for it in items:
        it["platforms"] = platforms_for(it)
    out = home() / "resources.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = {"synced_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "source": PAGE, "items": items}
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(items)} resources → {out}", file=sys.stderr)
    return out


def load() -> dict:
    for p in (home() / "resources.json", BUNDLED):
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    return {"items": []}


def match(items: list[dict], query: str) -> list[dict]:
    q = query.lower().replace("-", " ")
    words = q.split()
    def hay(it):
        return " ".join([it["section"], it["title"], it["description"],
                         *(l["label"] + " " + l["url"] for l in it["links"])]).lower().replace("-", " ")
    exact = [it for it in items if it["title"].lower().replace("-", " ") == q]
    return exact or [it for it in items if all(w in hay(it) for w in words)]


# --------------------------------------------------------------------------- download / install

def download(url: str, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = url.split("?")[0].rsplit("/", 1)[-1]
    dest = dest_dir / name
    if dest.exists() and dest.stat().st_size > 0:
        print(f"  already there: {dest}", file=sys.stderr)
        return dest
    print(f"  downloading {url}", file=sys.stderr)
    tmp = dest.with_suffix(dest.suffix + ".part")
    subprocess.run(["curl", "-fL", "--progress-bar", "-A", UA, "-o", str(tmp), url], check=True)
    tmp.rename(dest)
    return dest


def install_fonts_from_dmg(dmg: Path, target: Path) -> list[Path]:
    """Mount DMG, expand the contained .pkg without running it and copy fonts to ~/Library/Fonts."""
    installed = []
    with tempfile.TemporaryDirectory(prefix="apple-fonts-") as tmp:
        mnt = Path(tmp) / "mnt"
        mnt.mkdir()
        subprocess.run(["hdiutil", "attach", "-nobrowse", "-readonly", "-mountpoint", str(mnt), str(dmg)],
                       check=True, capture_output=True)
        try:
            for pkg in mnt.glob("*.pkg"):
                exp = Path(tmp) / pkg.stem
                subprocess.run(["pkgutil", "--expand-full", str(pkg), str(exp)], check=True, capture_output=True)
                for font in list(exp.rglob("*.otf")) + list(exp.rglob("*.ttf")):
                    dst = target / font.name
                    shutil.copy2(font, dst)
                    installed.append(dst)
        finally:
            subprocess.run(["hdiutil", "detach", str(mnt), "-quiet"], check=False)
    return installed


# --------------------------------------------------------------------------- commands

def cmd_list(args) -> int:
    items = load()["items"]
    if args.platform:
        items = [i for i in items if args.platform in i.get("platforms", []) or "all" in i.get("platforms", [])]
    if args.kind:
        items = [i for i in items if any(l["kind"] == args.kind for l in i["links"])
                 or (args.kind == "font" and i["section_id"] == "fonts")]
    if args.json:
        print(json.dumps(items, ensure_ascii=False, indent=1))
        return 0
    section = None
    for it in items:
        if it["section"] != section:
            section = it["section"]
            print(f"\n## {section}")
        kinds = ", ".join(sorted({l["kind"] for l in it["links"]}))
        print(f"- {it['title']}  [{kinds}]")
    return 0


def cmd_show(args) -> int:
    hits = match(load()["items"], args.query)
    if not hits:
        print("No resource found. Tip: `resources.py list`.", file=sys.stderr)
        return 1
    for it in hits:
        print(f"### {it['title']}  ({it['section']})")
        if it["description"]:
            print(it["description"])
        for l in it["links"]:
            note = f" — {l['note']}" if l["note"] else ""
            print(f"- {l['label']} [{l['kind']}]: {l['url']}{note}")
        print()
    return 0


def cmd_download(args) -> int:
    items = load()["items"]
    all_dmgs = sorted({l["url"] for it in items for l in it["links"] if l["kind"] == "dmg"})
    if args.query in PRESETS:
        urls = [u for u in all_dmgs if any(p in u for p in PRESETS[args.query])]
    elif args.query == "all":
        urls = all_dmgs
    else:
        urls = [l["url"] for it in match(items, args.query) for l in it["links"] if l["kind"] == "dmg"]
    if not urls:
        print("Kein DMG zu dieser Suche. Figma/Sketch-Vorlagen sind Links: `resources.py show`.", file=sys.stderr)
        return 1
    if not args.accept_license:
        print(LICENSE_NOTE + "\nTreffer:\n" + "\n".join(f"  {u}" for u in urls), file=sys.stderr)
        return 2
    for u in urls:
        print(download(u, home() / "downloads"))
    return 0


def cmd_install_fonts(args) -> int:
    if sys.platform != "darwin":
        print("Font installation is macOS only.", file=sys.stderr)
        return 1
    if not args.accept_license:
        print(LICENSE_NOTE, file=sys.stderr)
        return 2
    target = args.target or Path.home() / "Library" / "Fonts"
    target.mkdir(parents=True, exist_ok=True)
    total = 0
    for name in args.fonts or FONT_DMGS:
        url = f"https://devimages-cdn.apple.com/design/resources/download/{name}.dmg"
        dmg = download(url, home() / "downloads")
        fonts = install_fonts_from_dmg(dmg, target)
        total += len(fonts)
        print(f"{name}: {len(fonts)} font files → {target}")
    print(f"Installed {total} font files in total.")
    return 0


def cmd_status(args) -> int:
    d = home() / "downloads"
    files = sorted(d.glob("*.dmg")) if d.exists() else []
    print(f"Downloads ({d}):")
    for f in files:
        print(f"  {f.name}  {f.stat().st_size / 1e6:.0f} MB")
    if not files:
        print("  –")
    fonts = Path.home() / "Library" / "Fonts"
    fams = {"SF Pro": "SF-Pro", "SF Compact": "SF-Compact", "SF Mono": "SF-Mono", "New York": "NewYork"}
    print("Fonts in ~/Library/Fonts:")
    for fam, prefix in fams.items():
        n = len(list(fonts.glob(f"{prefix}*"))) if fonts.exists() else 0
        print(f"  {fam}: {n} files" + ("" if n else "  (not installed)"))
    cat = home() / "resources.json"
    print(f"Catalog: {cat if cat.exists() else BUNDLED}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list"); p.add_argument("--platform"); p.add_argument("--kind"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("show"); p.add_argument("query")
    sub.add_parser("sync")
    p = sub.add_parser("download"); p.add_argument("query"); p.add_argument("--accept-license", action="store_true")
    p = sub.add_parser("install-fonts"); p.add_argument("fonts", nargs="*"); p.add_argument("--accept-license", action="store_true")
    p.add_argument("--target", type=Path, help="target folder instead of ~/Library/Fonts")
    sub.add_parser("status")
    args = ap.parse_args()
    if args.cmd == "sync":
        sync()
        return 0
    return {"list": cmd_list, "show": cmd_show, "download": cmd_download,
            "install-fonts": cmd_install_fonts, "status": cmd_status}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
