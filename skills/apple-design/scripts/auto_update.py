#!/usr/bin/env python3
"""Keep the local HIG mirror and resource catalog fresh – called by the plugin's SessionStart hook.

    python3 auto_update.py            # detach and update in the background if stale (returns immediately)
    python3 auto_update.py --now      # run in the foreground (used by the detached child, or for testing)

Freshness check needs no network: it only reads timestamps. Defaults: HIG mirror older than 7 days,
resource catalog older than 30 days. Silent; log in $APPLE_DESIGN_HOME/update.log.
Opt out with APPLE_DESIGN_AUTO_UPDATE=0. Tune with APPLE_DESIGN_HIG_MAX_AGE / APPLE_DESIGN_RESOURCES_MAX_AGE (days).
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOME = Path(os.environ.get("APPLE_DESIGN_HOME", Path.home() / ".apple-design"))
LOCK = HOME / ".update.lock"
LOG = HOME / "update.log"


def age_days(path: Path, key: str | None = None) -> float:
    """Age of a synced file in days, from its JSON timestamp (or mtime); inf if missing."""
    if not path.exists():
        return float("inf")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        stamp = data["meta"]["synced_at"] if key == "meta" else data["synced_at"]
        synced = dt.datetime.fromisoformat(stamp)
        return (dt.datetime.now(dt.timezone.utc) - synced).total_seconds() / 86400
    except Exception:
        return (time.time() - path.stat().st_mtime) / 86400


def due() -> list[str]:
    jobs = []
    if age_days(HOME / "hig" / "index.json", "meta") >= float(os.environ.get("APPLE_DESIGN_HIG_MAX_AGE", 7)):
        jobs.append("hig")
    if age_days(HOME / "resources.json") >= float(os.environ.get("APPLE_DESIGN_RESOURCES_MAX_AGE", 30)):
        jobs.append("resources")
    return jobs


def run(jobs: list[str]) -> None:
    HOME.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as log:
        log.write(f"\n[{dt.datetime.now().isoformat(timespec='seconds')}] auto-update: {', '.join(jobs)}\n")
        log.flush()
        cmds = {"hig": [sys.executable, "-I", str(HERE / "hig_sync.py")],
                "resources": [sys.executable, "-I", str(HERE / "resources.py"), "sync"]}
        for job in jobs:
            res = subprocess.run(cmds[job], stdout=log, stderr=log)
            log.write(f"  {job}: exit {res.returncode}\n")
            log.flush()


def main() -> int:
    if os.environ.get("APPLE_DESIGN_AUTO_UPDATE", "1") == "0":
        return 0
    jobs = due()
    if not jobs:
        return 0
    # one updater at a time across parallel sessions; stale locks expire after 15 minutes
    if LOCK.exists() and time.time() - LOCK.stat().st_mtime < 900:
        return 0
    if "--now" in sys.argv:
        HOME.mkdir(parents=True, exist_ok=True)
        LOCK.write_text(str(os.getpid()))
        try:
            run(jobs)
        finally:
            LOCK.unlink(missing_ok=True)
        return 0
    subprocess.Popen([sys.executable, "-I", __file__, "--now"], stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # never disturb a session start
