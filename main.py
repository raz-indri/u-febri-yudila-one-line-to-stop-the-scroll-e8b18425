#!/usr/bin/env python3
"""One Line to Stop the Scroll.

Writes a single warm, human line to /output/entry.txt.
"""

import os

LINE = "My grandma just learned to text. She says hi, she says you look tired, and she says drink some water."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
