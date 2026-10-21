#!/usr/bin/env python3
"""Display specs of Apple devices, read from Xcode's simulator device profiles.

Apple removed the device specification tables from the HIG layout page (2026-09-09).
Xcode still ships exact values per device type: pixels, scale, points, corner radius.

    python3 device_specs.py                     # current iPhone, iPad and Watch models
    python3 device_specs.py --family watch      # iphone | ipad | watch | tv | vision
    python3 device_specs.py --all               # include legacy devices
    python3 device_specs.py --json

Needs Xcode (not just the Command Line Tools). Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
import plistlib
import subprocess
import sys
from pathlib import Path

FAMILIES = {"iphone": "iPhone", "ipad": "iPad", "watch": "Apple Watch", "tv": "Apple TV", "vision": "Apple Vision"}


def developer_dir() -> str | None:
    if os.environ.get("DEVELOPER_DIR"):
        return os.environ["DEVELOPER_DIR"]
    try:
        cur = subprocess.run(["xcode-select", "-p"], capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        return None
    if cur and "CommandLineTools" not in cur:
        return cur
    for app in sorted(Path("/Applications").glob("Xcode*.app"), reverse=True):
        dev = app / "Contents" / "Developer"
        if dev.exists():
            return str(dev)
    return None


def device_types() -> list[dict]:
    dev = developer_dir()
    if not dev:
        sys.exit("Xcode nicht gefunden. Gerätedaten brauchen Xcode (nicht nur die Command Line Tools).")
    env = dict(os.environ, DEVELOPER_DIR=dev)
    out = subprocess.run(["xcrun", "simctl", "list", "devicetypes", "-j"], capture_output=True, text=True, env=env)
    if out.returncode:
        sys.exit(out.stderr.strip() or "simctl fehlgeschlagen")
    return json.loads(out.stdout)["devicetypes"]


def spec(t: dict) -> dict | None:
    res = Path(t["bundlePath"]) / "Contents" / "Resources"
    try:
        caps = plistlib.load((res / "capabilities.plist").open("rb")).get("capabilities", {})
        prof = plistlib.load((res / "profile.plist").open("rb"))
    except Exception:
        return None
    dims = caps.get("ScreenDimensionsCapability", {})
    w, h = dims.get("main-screen-width"), dims.get("main-screen-height")
    scale = dims.get("main-screen-scale") or caps.get("ArtworkTraits", {}).get("ArtworkDeviceScaleFactor")
    try:
        w, h, scale = float(w), float(h), float(scale)
    except (TypeError, ValueError):
        return None
    return {
        "name": t["name"],
        "family": t.get("productFamily", ""),
        "px": f"{w:g}×{h:g}",
        "scale": f"@{scale:g}x",
        "pt": f"{w / scale:g}×{h / scale:g}",
        "ppi": dims.get("main-screen-pitch"),
        "corner_radius_pt": round(float(caps["DeviceCornerRadius"]), 1) if caps.get("DeviceCornerRadius") else None,
        "min_os": prof.get("minRuntimeVersion"),
        "max_os": prof.get("maxRuntimeVersion"),
        "model": prof.get("modelIdentifier"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--family", choices=FAMILIES)
    ap.add_argument("--all", action="store_true", help="auch Geräte, die aktuelle OS-Versionen nicht mehr unterstützen")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = [s for t in device_types() if (s := spec(t))]
    if args.family:
        rows = [r for r in rows if r["family"].lower().startswith(FAMILIES[args.family].lower())
                or r["name"].startswith(FAMILIES[args.family])]
    if not args.all:
        rows = [r for r in rows if not r["max_os"]]
    rows.sort(key=lambda r: (r["family"], r["min_os"] or "", r["name"]))
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    print(f"{'Gerät':<40} {'Punkte':>11} {'Pixel':>11} {'Scale':>6} {'Ecke pt':>8}  ab OS")
    fam = None
    for r in rows:
        if r["family"] != fam:
            fam = r["family"]
            print(f"— {fam}")
        print(f"{r['name']:<40} {r['pt']:>11} {r['px']:>11} {r['scale']:>6} {r['corner_radius_pt'] or '':>8}  {r['min_os']}")
    print("\nQuelle: Xcode-Simulatorprofile (" + (developer_dir() or "?") + "). Werte = Display, ohne Safe Areas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
