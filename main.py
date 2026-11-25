#!/usr/bin/env python3
"""Entry for the make.fun bounty "Two Robots in an Elevator".

Writes one funny line -- two robots making small talk in an elevator --
to /output/entry.txt as UTF-8 text with no trailing newline.
"""

import os

LINE = (
    "Nice weather we're having. My sensors cannot confirm this, but I "
    "enjoy saying it while we avoid eye contact we do not have."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path):
    """Write the line to path as UTF-8, with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    write_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
