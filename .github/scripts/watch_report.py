#!/usr/bin/env python3
"""Build the weekly HIG watch report for the GitHub Action.

Expects a fresh mirror and resource catalog in $APPLE_DESIGN_HOME. Writes the issue body to the path
given as first argument and prints `changes=true|false` for $GITHUB_OUTPUT.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "skills" / "apple-design"
HOME = Path(os.environ["APPLE_DESIGN_HOME"])


def stale() -> dict:
    out = subprocess.run([sys.executable, "-I", str(SKILL / "scripts" / "hig_search.py"), "stale", "--json"],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def resource_diff() -> tuple[list, list]:
    def keyset(path: Path) -> dict:
        items = json.loads(path.read_text(encoding="utf-8"))["items"]
        return {(i["section"], i["title"], l["url"]): l["label"] for i in items for l in i["links"]}
    old, new = keyset(SKILL / "data" / "resources.json"), keyset(HOME / "resources.json")
    return sorted(k for k in new if k not in old), sorted(k for k in old if k not in new)


def main() -> int:
    body_path = Path(sys.argv[1])
    r = stale()
    added, removed = resource_diff()
    n_hig = len(r["changed"]) + len(r["new"]) + len(r["removed"])
    if not n_hig and not added and not removed:
        print("changes=false")
        return 0

    lines = [
        "Automated weekly check of Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) "
        "and [Design Resources](https://developer.apple.com/design/resources/) against this repo.",
        "",
        f"- References reviewed (baseline): **{r['reviewed']}**",
        f"- HIG mirrored: {r['mirror_synced']}",
        "",
    ]
    for label, rows in (("Changed HIG pages", r["changed"]), ("New HIG pages", r["new"]),
                        ("Removed HIG pages", r["removed"])):
        if not rows:
            continue
        lines += [f"### {label} ({len(rows)})", "", "| Page | Changed | Change note | Affected references |", "|---|---|---|---|"]
        for x in rows:
            url = f"https://developer.apple.com/design/human-interface-guidelines/{x['slug']}"
            cited = "<br>".join(f"`{c}`" for c in x["cited_in"]) or "_not cited_"
            note = (x.get("note") or "").replace("|", "\\|")
            lines.append(f"| [{x['title']}]({url}) `hig:{x['slug']}` | {x.get('changed') or '–'} | {note} | {cited} |")
        lines.append("")
    if added or removed:
        lines += ["### Design Resources catalog", ""]
        for s, t, u in added:
            lines.append(f"- ➕ **{t}** ({s}): {u}")
        for s, t, u in removed:
            lines.append(f"- ➖ **{t}** ({s}): {u}")
        lines.append("")
    slugs = " ".join(x["slug"] for x in r["changed"] + r["new"] + r["removed"])
    lines += ["### To do", ""]
    if slugs:
        lines += ["- [ ] Read the changed pages (`hig_search.py page <slug>`) and update the affected reference files",
                  f"- [ ] Mark them reviewed: `python3 -I skills/apple-design/scripts/hig_search.py baseline {slugs}`"]
    if added or removed:
        lines.append("- [ ] Refresh the bundled catalog: `python3 -I skills/apple-design/scripts/resources.py sync && "
                     "cp ~/.apple-design/resources.json skills/apple-design/data/resources.json`")
    lines += ["- [ ] Bump the version in `.claude-plugin/plugin.json` and `marketplace.json`", "",
              "_This issue is updated by the `HIG watch` workflow and closes itself once everything matches again._"]
    body_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("changes=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
