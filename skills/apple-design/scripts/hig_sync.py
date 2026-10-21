#!/usr/bin/env python3
"""Mirror Apple's Human Interface Guidelines as local Markdown.

Crawls the public DocC JSON behind developer.apple.com/design/human-interface-guidelines,
renders every page to Markdown and writes a search index.

    python3 hig_sync.py                 # sync into $APPLE_DESIGN_HOME/hig (default ~/.apple-design/hig)
    python3 hig_sync.py --out ./hig     # custom target
    python3 hig_sync.py --if-stale 14   # only sync when the mirror is older than 14 days

The mirror is for personal reference. The content stays © Apple Inc.; do not redistribute it.
Stdlib only, no third-party dependencies.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import re
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://developer.apple.com"
DATA = BASE + "/tutorials/data"
ROOT = "/design/human-interface-guidelines"
UA = "apple-design-plugin/1.0 (+personal HIG mirror)"


def home() -> Path:
    return Path(os.environ.get("APPLE_DESIGN_HOME", Path.home() / ".apple-design"))


_USE_CURL = False


def http_get(url: str, timeout: int = 30) -> bytes:
    """GET via urllib; falls back to curl (system trust store) behind TLS-inspecting proxies."""
    global _USE_CURL
    if not _USE_CURL:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.URLError as e:
            if "CERTIFICATE_VERIFY_FAILED" not in str(e) or not shutil.which("curl"):
                raise
            _USE_CURL = True
    res = subprocess.run(["curl", "-sSfL", "--max-time", str(timeout), "-A", UA, url],
                         capture_output=True)
    if res.returncode == 22:
        raise urllib.error.HTTPError(url, 404, "not found", None, None)
    if res.returncode:
        raise OSError(res.stderr.decode(errors="replace").strip())
    return res.stdout


def fetch_json(path: str, retries: int = 3) -> dict | None:
    url = f"{DATA}{path}.json"
    for attempt in range(retries):
        try:
            return json.loads(http_get(url))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(1.5 * (attempt + 1))
    return None


# --------------------------------------------------------------------------- rendering

class Renderer:
    def __init__(self, doc: dict):
        self.refs = doc.get("references", {})

    def ref_link(self, ident: str, title: str | None = None) -> str:
        ref = self.refs.get(ident, {})
        url = ref.get("url") or ""
        text = title or ref.get("title") or ident.rsplit("/", 1)[-1]
        if url.startswith(ROOT + "/"):
            return f"[{text}](hig:{url[len(ROOT) + 1:]})"
        if url.startswith("/"):
            url = BASE + url
        return f"[{text}]({url})" if url else text

    def image(self, ident: str) -> str:
        ref = self.refs.get(ident, {})
        alt = (ref.get("alt") or "").strip()
        variants = ref.get("variants") or []
        url = next((v["url"] for v in variants if "light" in v.get("traits", [])), None) or (
            variants[0]["url"] if variants else "")
        if url.startswith("/"):
            url = BASE + url
        if not alt and not url:
            return ""
        return f"![{alt}]({url})" if url else f"*[Image: {alt}]*"

    def inline(self, items: list) -> str:
        out = []
        for it in items or []:
            t = it.get("type")
            if t == "text":
                out.append(it.get("text", ""))
            elif t == "codeVoice":
                out.append(f"`{it.get('code', '')}`")
            elif t == "emphasis":
                out.append(f"*{self.inline(it.get('inlineContent'))}*")
            elif t == "strong":
                out.append(f"**{self.inline(it.get('inlineContent'))}**")
            elif t == "reference":
                out.append(self.ref_link(it["identifier"], it.get("overridingTitle")))
            elif t == "link":
                out.append(f"[{it.get('title') or it.get('destination')}]({it.get('destination')})")
            elif t == "image":
                out.append(self.image(it["identifier"]))
            elif t == "newTerm":
                out.append(f"*{self.inline(it.get('inlineContent'))}*")
            elif t in ("superscript", "subscript", "strikethrough"):
                out.append(self.inline(it.get("inlineContent")))
            elif "inlineContent" in it:
                out.append(self.inline(it["inlineContent"]))
        return "".join(out)

    def blocks(self, items: list, depth: int = 0) -> list[str]:
        out: list[str] = []
        for b in items or []:
            t = b.get("type")
            if t == "heading":
                out.append("#" * min(6, b.get("level", 2)) + " " + b.get("text", ""))
            elif t == "paragraph":
                txt = self.inline(b.get("inlineContent")).strip()
                if txt:
                    out.append(txt)
            elif t in ("unorderedList", "orderedList"):
                lines = []
                for i, item in enumerate(b.get("items", []), 1):
                    bullet = f"{i}." if t == "orderedList" else "-"
                    body = self.blocks(item.get("content", []), depth + 1)
                    first, *rest = (body or [""])
                    lines.append(f"{bullet} {first}")
                    lines.extend("  " + ln for r in rest for ln in r.splitlines())
                out.append("\n".join(lines))
            elif t == "aside":
                name = b.get("name") or b.get("style", "Note").title()
                body = "\n\n".join(self.blocks(b.get("content", []), depth + 1))
                out.append("\n".join(f"> {ln}" if ln else ">" for ln in f"**{name}:** {body}".splitlines()))
            elif t == "codeListing":
                out.append(f"```{b.get('syntax') or ''}\n" + "\n".join(b.get("code", [])) + "\n```")
            elif t == "table":
                out.append(self.table(b))
            elif t == "row":
                for col in b.get("columns", []):
                    out.extend(self.blocks(col.get("content", []), depth + 1))
            elif t == "tabNavigator":
                for tab in b.get("tabs", []):
                    out.append(f"**{tab.get('title')}**")
                    out.extend(self.blocks(tab.get("content", []), depth + 1))
            elif t == "termList":
                for item in b.get("items", []):
                    term = self.inline(item.get("term", {}).get("inlineContent"))
                    defin = " ".join(self.blocks(item.get("definition", {}).get("content", [])))
                    out.append(f"- **{term}** — {defin}")
            elif t == "links":
                out.append("\n".join(f"- {self.ref_link(i)}" for i in b.get("items", [])))
            elif t == "small":
                out.append(f"<small>{self.inline(b.get('inlineContent'))}</small>")
            elif t == "video":
                ref = self.refs.get(b.get("identifier", ""), {})
                alt = ref.get("alt") or "Video"
                out.append(f"*[Video: {alt}]*")
            elif "content" in b:
                out.extend(self.blocks(b["content"], depth + 1))
        return out

    def table(self, b: dict) -> str:
        rows = []
        for row in b.get("rows", []):
            cells = []
            for cell in row:
                txt = " ".join(self.blocks(cell)).replace("\n", " ").replace("|", "\\|")
                cells.append(txt.strip())
            rows.append(cells)
        if not rows:
            return ""
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        if b.get("header") in ("row", "both"):
            head, body = rows[0], rows[1:]
        else:
            head, body = [""] * width, rows
        lines = ["| " + " | ".join(head) + " |", "|" + "---|" * width]
        lines += ["| " + " | ".join(r) + " |" for r in body]
        return "\n".join(lines)


def render_page(path: str, doc: dict) -> tuple[str, dict]:
    r = Renderer(doc)
    meta = doc.get("metadata", {})
    custom = meta.get("customMetadata", {}) or {}
    title = meta.get("title") or path.rsplit("/", 1)[-1]
    abstract = r.inline(doc.get("abstract")).strip()
    platforms = [p for p in (custom.get("supported-platforms") or "").split(",") if p]
    slug = path[len(ROOT) + 1:] if path.startswith(ROOT + "/") else "index"

    md = [f"# {title}", ""]
    md.append(f"<!-- source: {BASE}{path} · © Apple Inc. · mirrored {dt.date.today().isoformat()} -->")
    if platforms:
        md.append(f"**Platforms:** {', '.join(platforms)}")
    if custom.get("alert-text"):
        md.append(f"**Update {custom.get('alert-date', '')}:** {custom['alert-text']}")
    md.append("")
    if abstract:
        md += [f"> {abstract}", ""]
    headings = []
    for sec in doc.get("primaryContentSections", []):
        content = sec.get("content", [])
        headings += [h.get("text") for h in content if h.get("type") == "heading"]
        md.append("\n\n".join(r.blocks(content)))
    for sec in doc.get("topicSections", []) or []:
        md.append(f"\n## {sec.get('title') or 'Topics'}")
        md.append("\n".join(f"- {r.ref_link(i)}" for i in sec.get("identifiers", [])))
    for sec in doc.get("seeAlsoSections", []) or []:
        md.append(f"\n## {sec.get('title') or 'See also'}")
        md.append("\n".join(f"- {r.ref_link(i)}" for i in sec.get("identifiers", [])))

    entry = {
        "slug": slug,
        "title": title,
        "abstract": abstract,
        "platforms": platforms,
        "url": BASE + path,
        "headings": headings,
        "updated": custom.get("alert-date"),
        "update_note": custom.get("alert-text"),
    }
    entry.update(change_info(md, custom))
    entry["hash"] = content_hash(md)
    return "\n".join(md).rstrip() + "\n", entry


def content_hash(md: list[str]) -> str:
    """Fingerprint of the page content, ignoring the per-sync source comment."""
    body = "\n".join(l for l in md if not l.startswith("<!-- source:"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]


def change_info(md: list[str], custom: dict) -> dict:
    """Latest change from the page's change log table, falling back to the alert metadata."""
    text = "\n".join(md)
    log = text.split("## Change log", 1)[1] if "## Change log" in text else ""
    best = None
    for date_s, note in re.findall(r"^\| ([A-Z][a-z]+ \d{1,2}, \d{4}) \| (.*?) \|$", log, re.M):
        try:
            d = dt.datetime.strptime(date_s, "%B %d, %Y").date().isoformat()
        except ValueError:
            continue
        if not best or d > best[0]:
            best = (d, note)
    alert = custom.get("alert-date")
    if alert and (not best or alert > best[0]):
        best = (alert, custom.get("alert-text") or "")
    return {"changed": best[0] if best else None, "change_note": best[1] if best else None}


def child_paths(doc: dict) -> set[str]:
    out = set()
    for ref in doc.get("references", {}).values():
        url = ref.get("url") or ""
        if ref.get("type") == "topic" and url.startswith(ROOT + "/"):
            out.add(url.split("#", 1)[0])
    return out


def topic_tree(doc: dict) -> list[dict]:
    refs = doc.get("references", {})
    tree = []
    for sec in doc.get("topicSections", []) or []:
        items = []
        for ident in sec.get("identifiers", []):
            url = refs.get(ident, {}).get("url", "")
            if url.startswith(ROOT + "/"):
                items.append(url[len(ROOT) + 1:])
        tree.append({"title": sec.get("title"), "pages": items})
    return tree


# --------------------------------------------------------------------------- main

def sync(out: Path, workers: int) -> int:
    pages_dir = out / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    root = fetch_json(ROOT)
    if not root:
        print("Could not load the HIG start page.", file=sys.stderr)
        return 1

    seen: set[str] = {ROOT}
    queue = sorted(child_paths(root))
    seen.update(queue)
    docs: dict[str, dict] = {ROOT: root}

    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        while queue:
            batch, queue = queue, []
            for path, doc in zip(batch, pool.map(fetch_json, batch)):
                if not doc:
                    print(f"  ! missing: {path}", file=sys.stderr)
                    continue
                docs[path] = doc
                for child in child_paths(doc):
                    if child not in seen:
                        seen.add(child)
                        queue.append(child)
            print(f"  {len(docs)} pages loaded …", file=sys.stderr)

    index = []
    for path, doc in sorted(docs.items()):
        md, entry = render_page(path, doc)
        (pages_dir / f"{entry['slug']}.md").write_text(md, encoding="utf-8")
        index.append(entry)

    # Section membership: landing page → chapters (Foundations, Patterns, …) → pages
    titles = {e["slug"]: e["title"] for e in index}
    sections: dict[str, list[str]] = {}
    page_section: dict[str, str] = {}

    def assign(slug: str, trail: str, chapter: str) -> None:
        for sub in topic_tree(docs.get(f"{ROOT}/{slug}", {})):
            for child in sub["pages"]:
                if child in page_section:
                    continue
                here = f"{trail} / {sub['title']}" if sub.get("title") else trail
                page_section[child] = here
                sections.setdefault(chapter, []).append(child)
                assign(child, f"{trail} / {titles.get(child, child)}", chapter)

    for chapter in (s for sec in topic_tree(root) for s in sec["pages"]):
        name = titles.get(chapter, chapter)
        page_section[chapter] = name
        assign(chapter, name, name)
    for e in index:
        e["section"] = page_section.get(e["slug"], "")

    meta = {
        "synced_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "source": BASE + ROOT,
        "pages": len(index),
        "sections": sections,
        "copyright": "Content © Apple Inc. Personal reference mirror – do not redistribute.",
    }
    (out / "index.json").write_text(json.dumps({"meta": meta, "pages": index}, ensure_ascii=False, indent=1),
                                    encoding="utf-8")
    print(f"Done: {len(index)} pages → {out}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=home() / "hig")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--if-stale", type=int, metavar="DAYS",
                    help="only sync if the mirror is older than DAYS days or missing")
    args = ap.parse_args()

    idx = args.out / "index.json"
    if args.if_stale is not None and idx.exists():
        try:
            synced = dt.datetime.fromisoformat(json.loads(idx.read_text())["meta"]["synced_at"])
            age = (dt.datetime.now(dt.timezone.utc) - synced).days
            if age < args.if_stale:
                print(f"HIG mirror is current ({age} days old): {args.out}", file=sys.stderr)
                return 0
        except Exception:
            pass
    return sync(args.out, args.workers)


if __name__ == "__main__":
    sys.exit(main())
