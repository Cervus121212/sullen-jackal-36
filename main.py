#!/usr/bin/env python3
"""One-line resignation letter of a log rotator.

Writes the single final line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, deterministic, no trailing newline.
"""

import os

PART_A = "I resign. I have deleted the evidence of every mistake "
PART_B = "for three years, and tonight I am keeping a copy for myself."


def compose_line() -> str:
    """Assemble the resignation line from its two parts."""
    return PART_A + PART_B


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(compose_line())


if __name__ == "__main__":
    main()
