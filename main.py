#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one funny line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, stdlib only, deterministic, no network.
"""

import os
from pathlib import Path

LINE = (
    "My screen time report just filed a restraining order against me — "
    "nine hours a day apparently counts as stalking myself."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} characters, must be 1-200")
    # The entry must stand alone as a single sentence: one line, no
    # line breaks, exactly one terminal full stop.
    if "\n" in text or text.count(".") != 1 or not text.endswith("."):
        raise ValueError("line must be a single sentence")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
