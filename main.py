"""The One-Liner Groan-Off entry: one original dad joke, one line.

Writes the line deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, no network, no randomness, no clock.
"""

import os

ENTRY = "My wife says my snoring sounds like a chainsaw \u2014 I told her it's just my body logging some sleep."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
