#!/usr/bin/env python3
"""Warning Label for Humans — write one label line to entry.txt.

The bounty asks for a single-line safety warning label that should
come printed on every human being, at most 160 characters, funny
first and plausible second. This program writes exactly that label,
and nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

# The label, written for this bounty: it sounds like a real printed
# label in wording and rhythm (WARNING, runs on, overheats, may...),
# it is true about people in general, and the laugh lands in the last
# few words.
LINE = (
    "WARNING: This human runs on caffeine and spite, overheats in "
    "small talk, and may spontaneously start a new hobby at 2 a.m."
)


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-160 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One line only, no
    # line breaks inside the line.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())