#!/usr/bin/env python3
"""Merge synthetic forensic artifact CSVs into one chronological timeline."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "sample-data"
INPUT_FILES = [
    DATA_DIR / "browser_history.csv",
    DATA_DIR / "usb_events.csv",
    DATA_DIR / "file_activity.csv",
]
OUTPUT_FILE = DATA_DIR / "generated_timeline.csv"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def read_events(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def main() -> None:
    events: list[dict[str, str]] = []

    for input_file in INPUT_FILES:
        events.extend(read_events(input_file))

    events.sort(key=lambda item: datetime.strptime(item["timestamp"], TIME_FORMAT))

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["timestamp", "source", "event", "details"],
        )
        writer.writeheader()
        writer.writerows(events)

    print(f"Timeline created: {OUTPUT_FILE}")
    print(f"Events written: {len(events)}")


if __name__ == "__main__":
    main()
