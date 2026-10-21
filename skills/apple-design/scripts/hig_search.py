#!/usr/bin/env python3
"""Query the local Human Interface Guidelines mirror (see hig_sync.py).

    python3 hig_search.py search "tab bar badge" [--platform ios] [--limit 8]
    python3 hig_search.py page buttons [--section "Platform considerations"]
    python3 hig_search.py platform watchos [--page buttons]   # every "Platform considerations" block for one OS
    python3 hig_search.py list [--section Components]
    python3 hig_search.py updates [--since 2025-06-01]        # recently changed guidance
    python3 hig_search.py stale [--brief|--json]              # HIG pages changed since the references were reviewed
    python3 hig_search.py baseline [slug …]                   # maintainers: mark pages as reviewed

Pages are addressed by slug (the last URL segment); references inside the mirror use `hig:<slug>`.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

PLATFORM_NAMES = {"ios": "iOS", "ipados": "iPadOS", "macos": "macOS", "watchos": "watchOS",
                  "tvos": "tvOS", "visionos": "visionOS"}


SKILL_DIR = Path(__file__).resolve().parent.parent
BASELINE = SKILL_DIR / "data" / "hig-baseline.json"


def mirror() -> Path:
    return Path(os.environ.get("APPLE_DESIGN_HOME", Path.home() / ".apple-design")) / "hig"


def load_index() -> dict:
    idx = mirror() / "index.json"
    if not idx.exists():
        sync = Path(__file__).with_name("hig_sync.py")
        print("HIG mirror missing – syncing once …", file=sys.stderr)
        subprocess.run([sys.executable, "-I", str(sync)], check=True)
    return json.loads(idx.read_text(encoding="utf-8"))


def read_page(slug: str) -> str:
    p = mirror() / "pages" / f"{slug}.md"
    if not p.exists():
        raise SystemExit(f"Page '{slug}' not in the mirror. `hig_search.py list` shows all slugs.")
    return p.read_text(encoding="utf-8")


def sections(md: str) -> list[tuple[int, str, str]]:
    """Split Markdown into (level, heading, body) blocks."""
    out, level, head, buf = [], 1, "", []
    for line in md.splitlines():
        m = re.match(r"^(#{1,6}) (.+)$", line)
        if m:
            out.append((level, head, "\n".join(buf)))
            level, head, buf = len(m.group(1)), m.group(2).strip(), []
        else:
            buf.append(line)
    out.append((level, head, "\n".join(buf)))
    return out


def extract(md: str, heading: str) -> str:
    """Return a heading and everything nested below it."""
    lines = md.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6}) (.+)$", line)
        if m and m.group(2).strip().lower() == heading.lower():
            lvl = len(m.group(1))
            end = next((j for j in range(i + 1, len(lines))
                        if (n := re.match(r"^(#{1,6}) ", lines[j])) and len(n.group(1)) <= lvl), len(lines))
            return "\n".join(lines[i:end]).strip()
    return ""


def strip_images(md: str) -> str:
    return re.sub(r"!\[([^\]]*)\]\([^)]+\)", lambda m: f"[Image: {m.group(1)[:90]}]" if m.group(1) else "", md)


# --------------------------------------------------------------------------- commands

def cmd_search(args) -> int:
    data = load_index()
    terms = [t.lower() for t in re.findall(r"\w[\w-]*", " ".join(args.query))]
    results = []
    for e in data["pages"]:
        if args.platform and e["platforms"] and args.platform not in e["platforms"]:
            continue
        md = read_page(e["slug"])
        low = md.lower()
        title = e["title"].lower()
        s = 0
        for t in terms:
            n = low.count(t)
            if not n:
                s = 0
                break
            s += min(n, 20) + (30 if t in title else 0) + (10 if t in e["slug"] else 0) \
                + (5 if any(t in h.lower() for h in e["headings"]) else 0)
        if not s:
            continue
        # best paragraph: most distinct terms, prefer bold-led rules
        best, best_s, best_head = "", 0, ""
        for _, head, body in sections(md):
            for para in re.split(r"\n\s*\n", body):
                pl = para.lower()
                ps = sum(t in pl for t in terms) * 10 + (3 if para.startswith("**") else 0)
                if ps > best_s and not para.startswith("!["):
                    best, best_s, best_head = para, ps, head
        results.append((s, e, best_head, best))
    results.sort(key=lambda r: -r[0])
    if not results:
        print("No matches.")
        return 1
    for s, e, head, para in results[:args.limit]:
        snippet = re.sub(r"\s+", " ", strip_images(para))[:400]
        plats = ",".join(e["platforms"]) or "–"
        print(f"## {e['title']}  (hig:{e['slug']})  [{plats}]")
        print(f"   {e['abstract']}")
        if snippet:
            print(f"   › {head}: {snippet}")
        print()
    return 0


def cmd_page(args) -> int:
    md = read_page(args.slug)
    if args.section:
        part = extract(md, args.section)
        if not part:
            heads = [h for _, h, _ in sections(md) if h]
            raise SystemExit(f"Section not found. Available: {', '.join(heads)}")
        md = part
    print(md if args.images else strip_images(md))
    return 0


def cmd_platform(args) -> int:
    data = load_index()
    name = PLATFORM_NAMES.get(args.platform.lower(), args.platform)
    count = 0
    for e in data["pages"]:
        if args.page and e["slug"] != args.page:
            continue
        md = read_page(e["slug"])
        pc = extract(md, "Platform considerations")
        if not pc:
            continue
        blocks = []
        for lvl, head, body in sections(pc):
            names = [h.strip() for h in re.split(r",| and ", head)]
            if name in names or head == name:
                blocks.append(body.strip())
        if blocks:
            count += 1
            print(f"## {e['title']}  (hig:{e['slug']})")
            print(strip_images("\n\n".join(blocks)), "\n")
    if not count:
        print(f"No platform-specific sections for {name}.")
    return 0


def cmd_list(args) -> int:
    data = load_index()
    cur = None
    for e in sorted(data["pages"], key=lambda e: (e["section"], e["title"])):
        if args.section and not e["section"].lower().startswith(args.section.lower()):
            continue
        if args.platform and e["platforms"] and args.platform not in e["platforms"]:
            continue
        if e["section"] != cur:
            cur = e["section"]
            print(f"\n### {cur or 'Start'}")
        print(f"- {e['slug']:<34} {e['title']} — {e['abstract'][:90]}")
    print(f"\nMirror: {mirror()} · synced {data['meta']['synced_at']}")
    return 0


def cmd_updates(args) -> int:
    data = load_index()
    rows = [e for e in data["pages"] if e.get("updated") and (not args.since or e["updated"] >= args.since)]
    for e in sorted(rows, key=lambda e: e["updated"], reverse=True):
        print(f"{e['updated']}  {e['title']:<32} hig:{e['slug']:<30} {e.get('update_note') or ''}")
    return 0


def citations() -> dict[str, list[str]]:
    """slug → reference files (relative to reference/) that cite it."""
    out: dict[str, set] = {}
    root = SKILL_DIR / "reference"
    for f in root.rglob("*.md"):
        for slug in set(re.findall(r"hig:([a-z0-9-]+)", f.read_text(encoding="utf-8"))):
            out.setdefault(slug, set()).add(str(f.relative_to(root)))
    return {k: sorted(v) for k, v in out.items()}


def compare() -> dict:
    data = load_index()
    if not BASELINE.exists():
        raise SystemExit(f"No baseline at {BASELINE}. Create one with `hig_search.py baseline`.")
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    cites = citations()
    now = {e["slug"]: e for e in data["pages"]}
    changed, new = [], []
    for slug, e in now.items():
        b = base["pages"].get(slug)
        if b is None:
            new.append({"slug": slug, "title": e["title"], "changed": e.get("changed"),
                        "note": e.get("change_note"), "cited_in": cites.get(slug, [])})
        elif b["hash"] != e.get("hash"):
            changed.append({"slug": slug, "title": e["title"], "changed": e.get("changed"),
                            "note": e.get("change_note") if (e.get("changed") or "") > (b.get("changed") or "")
                            else "no change log entry – silent edit", "cited_in": cites.get(slug, [])})
    removed = [{"slug": s, "title": b["title"], "cited_in": cites.get(s, [])}
               for s, b in base["pages"].items() if s not in now]
    key = lambda r: (r.get("changed") or "", r["slug"])
    return {"reviewed": base["reviewed"], "mirror_synced": data["meta"]["synced_at"],
            "changed": sorted(changed, key=key, reverse=True), "new": sorted(new, key=key, reverse=True),
            "removed": removed}


def cmd_stale(args) -> int:
    r = compare()
    total = len(r["changed"]) + len(r["new"]) + len(r["removed"])
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0
    if args.brief:
        if not total:
            print(f"apple-design: references match the HIG (reviewed {r['reviewed']}).")
        else:
            slugs = [x["slug"] for x in r["changed"] + r["new"] + r["removed"]]
            print(f"apple-design: {total} HIG page(s) changed since the references were reviewed "
                  f"({r['reviewed']}): {', '.join(slugs[:15])}{' …' if len(slugs) > 15 else ''}. "
                  f"For these, read the original page (`hig_search.py page <slug>`) – it wins over the reference.")
        return 0
    print(f"References reviewed: {r['reviewed']} · mirror synced: {r['mirror_synced']}\n")
    if not total:
        print("No HIG changes since the last review.")
        return 0
    for label, rows in (("Changed", r["changed"]), ("New pages", r["new"]), ("Removed pages", r["removed"])):
        if not rows:
            continue
        print(f"## {label} ({len(rows)})")
        for x in rows:
            date = f" · {x['changed']}" if x.get("changed") else ""
            note = f" – {x['note']}" if x.get("note") else ""
            cited = ", ".join(x["cited_in"]) or "not cited by any reference"
            print(f"- hig:{x['slug']} ({x['title']}){date}{note}\n    affects: {cited}")
        print()
    return 0


def cmd_baseline(args) -> int:
    data = load_index()
    now = {e["slug"]: e for e in data["pages"]}
    base = json.loads(BASELINE.read_text(encoding="utf-8")) if BASELINE.exists() else {"pages": {}}
    slugs = args.slugs or list(now)
    for s in slugs:
        if s in now:
            e = now[s]
            base["pages"][s] = {"title": e["title"], "hash": e.get("hash"), "changed": e.get("changed")}
        else:
            base["pages"].pop(s, None)
    if not args.slugs:
        base["pages"] = {s: v for s, v in base["pages"].items() if s in now}
    base["reviewed"] = dt.date.today().isoformat()
    base["pages"] = dict(sorted(base["pages"].items()))
    BASELINE.write_text(json.dumps(base, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Baseline updated for {len(slugs)} page(s) → {BASELINE}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search"); p.add_argument("query", nargs="+"); p.add_argument("--platform")
    p.add_argument("--limit", type=int, default=8)
    p = sub.add_parser("page"); p.add_argument("slug"); p.add_argument("--section"); p.add_argument("--images", action="store_true")
    p = sub.add_parser("platform"); p.add_argument("platform"); p.add_argument("--page")
    p = sub.add_parser("list"); p.add_argument("--section"); p.add_argument("--platform")
    p = sub.add_parser("updates"); p.add_argument("--since")
    p = sub.add_parser("stale"); p.add_argument("--brief", action="store_true"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("baseline"); p.add_argument("slugs", nargs="*")
    args = ap.parse_args()
    return {"search": cmd_search, "page": cmd_page, "platform": cmd_platform, "list": cmd_list,
            "updates": cmd_updates, "stale": cmd_stale, "baseline": cmd_baseline}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
