#!/usr/bin/env python3
"""Search SF Symbols by name, keyword or category – with minimum OS versions.

Reads the symbol metadata that ships with macOS (CoreGlyphs.bundle) or, if installed,
with the SF Symbols app. No network, stdlib only.

    python3 sf_symbols.py search heart            # names + search keywords
    python3 sf_symbols.py search "trash" --min-ios 17
    python3 sf_symbols.py info heart.fill         # availability, categories, aliases, fill variant
    python3 sf_symbols.py categories              # list categories
    python3 sf_symbols.py category health --limit 50
    python3 sf_symbols.py new 2025                # symbols introduced in a release year
"""
from __future__ import annotations

import argparse
import json
import plistlib
import sys
from pathlib import Path

SOURCES = [
    Path("/Applications/SF Symbols.app/Contents/Resources/Metadata"),
    Path("/System/Library/CoreServices/CoreGlyphs.bundle/Contents/Resources"),
]
PLATFORMS = ("iOS", "macOS", "watchOS", "tvOS", "visionOS")


def load_plist(base: Path, name: str):
    p = base / name
    if not p.exists():
        return None
    with p.open("rb") as f:
        try:
            return plistlib.load(f)
        except Exception:
            return None


class DB:
    def __init__(self):
        self.base = next((b for b in SOURCES if (b / "name_availability.plist").exists()), None)
        if not self.base:
            sys.exit("SF Symbols metadata not found (macOS only). "
                     "Alternatively install the SF Symbols app: resources.py show 'sf symbols'")
        avail = load_plist(self.base, "name_availability.plist") or {}
        self.year_of: dict[str, str] = avail.get("symbols", {})
        self.releases: dict[str, dict] = avail.get("year_to_release", {})
        self.keywords: dict[str, list] = load_plist(self.base, "symbol_search.plist") or {}
        self.cats_of: dict[str, list] = load_plist(self.base, "symbol_categories.plist") or {}
        self.categories = [c.get("key") for c in (load_plist(self.base, "categories.plist") or [])]
        self.restricted: dict = load_plist(self.base, "symbol_restrictions.strings") or {}
        aliases = load_plist(self.base, "name_aliases.strings") or {}
        self.aliases_of: dict[str, list] = {}
        for old, new in aliases.items():
            self.aliases_of.setdefault(new, []).append(old)
        self.fill: dict = load_plist(self.base, "nofill_to_fill.strings") or {}

    def min_os(self, name: str) -> dict:
        return self.releases.get(self.year_of.get(name, ""), {})

    def available(self, name: str, platform: str, version: str | None) -> bool:
        if not version:
            return True
        have = self.min_os(name).get(platform)
        if not have:
            return False
        return tuple(int(x) for x in have.split(".")) <= tuple(int(x) for x in version.split("."))

    def row(self, name: str) -> dict:
        r = {"name": name, "since": self.year_of.get(name), "min": self.min_os(name),
             "categories": self.cats_of.get(name, []), "keywords": self.keywords.get(name, [])}
        if name in self.restricted:
            r["restriction"] = self.restricted[name]
        if name in self.fill:
            r["fill_variant"] = self.fill[name]
        if name in self.aliases_of:
            r["deprecated_aliases"] = self.aliases_of[name]
        return r


def score(db: DB, name: str, terms: list[str]) -> int:
    s = 0
    kws = " ".join(db.keywords.get(name, [])).lower()
    for t in terms:
        if name == t:
            s += 100
        elif name.startswith(t + ".") or name.split(".")[0] == t:
            s += 40
        elif t in name.split("."):
            s += 25
        elif t in name:
            s += 10
        elif t in kws:
            s += 8
        else:
            return 0
    # prefer simple base symbols over locale/variant suffixes
    s -= name.count(".") + (5 if name.rsplit(".", 1)[-1] in {"ar", "hi", "he", "zh", "ja", "ko", "th", "rtl"} else 0)
    return s


def fmt(r: dict, verbose: bool = False) -> str:
    m = r["min"]
    v = " ".join(f"{p} {m[p]}" for p in ("iOS", "macOS", "watchOS") if p in m)
    line = f"{r['name']:<42} {v}"
    if r.get("restriction"):
        line += "  ⚠ restricted"
    if verbose:
        extra = []
        if r["categories"]:
            extra.append("Categories: " + ", ".join(r["categories"]))
        if r["keywords"]:
            extra.append("Keywords: " + ", ".join(r["keywords"]))
        if r.get("fill_variant"):
            extra.append("Fill variant: " + r["fill_variant"])
        if r.get("deprecated_aliases"):
            extra.append("Former names: " + ", ".join(r["deprecated_aliases"]))
        if r.get("restriction"):
            extra.append("Restriction: " + str(r["restriction"]))
        line += "".join(f"\n    {e}" for e in extra)
    return line


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search"); p.add_argument("query", nargs="+")
    for q in (p,):
        q.add_argument("--limit", type=int, default=30)
        q.add_argument("--min-ios"); q.add_argument("--min-macos"); q.add_argument("--min-watchos")
        q.add_argument("--no-locale", action="store_true", default=True)
    p = sub.add_parser("info"); p.add_argument("name")
    sub.add_parser("categories")
    p = sub.add_parser("category"); p.add_argument("key"); p.add_argument("--limit", type=int, default=100)
    p = sub.add_parser("new"); p.add_argument("year")
    args = ap.parse_args()
    db = DB()

    if args.cmd == "search":
        terms = [t.lower() for t in " ".join(args.query).split()]
        names = [n for n in db.year_of if score(db, n, terms) > 0]
        for plat, ver in (("iOS", args.min_ios), ("macOS", args.min_macos), ("watchOS", args.min_watchos)):
            names = [n for n in names if db.available(n, plat, ver)]
        names.sort(key=lambda n: -score(db, n, terms))
        rows = [db.row(n) for n in names[:args.limit]]
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=1))
        else:
            print("\n".join(fmt(r) for r in rows) or "No matches.")
            if len(names) > args.limit:
                print(f"… {len(names) - args.limit} more (--limit)")
    elif args.cmd == "info":
        if args.name not in db.year_of:
            close = [n for n in db.year_of if args.name in n][:10]
            print(f"'{args.name}' not found." + (f" Similar: {', '.join(close)}" if close else ""))
            return 1
        r = db.row(args.name)
        print(json.dumps(r, ensure_ascii=False, indent=1) if args.json else fmt(r, verbose=True))
    elif args.cmd == "categories":
        print("\n".join(db.categories))
    elif args.cmd == "category":
        names = [n for n, c in db.cats_of.items() if args.key in c]
        print("\n".join(fmt(db.row(n)) for n in names[:args.limit]))
        print(f"({len(names)} symbols in '{args.key}')")
    elif args.cmd == "new":
        names = sorted(n for n, y in db.year_of.items() if y.split(".")[0] == args.year)
        print("\n".join(fmt(db.row(n)) for n in names))
        print(f"({len(names)} symbols from {args.year}; release map: {db.releases.get(args.year, {})})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
