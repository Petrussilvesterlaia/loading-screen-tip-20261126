#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single original loading-screen tip to /output/entry.txt.
Deterministic, standard library only, no network, no model calls.
"""

import os

TIP = "Your AI just deleted the file it swore it backed up. Breathe \u2014 git remembers, and so will you, next time."

OUTPUT_PATH = "/output/entry.txt"


def validate_tip(tip: str) -> None:
    """Enforce the competition gate before anything is written.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 200 characters, not only white space, on a single line.
    """
    if not tip or not tip.strip():
        raise ValueError("tip must not be empty or only white space")
    if "\n" in tip or "\r" in tip:
        raise ValueError("tip must be a single line")
    if len(tip) > 200:
        raise ValueError("tip is %d characters, over the 200 limit" % len(tip))


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it holds exactly the validated tip."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != expected:
        raise ValueError("entry.txt does not match the validated tip")


def main() -> int:
    validate_tip(TIP)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TIP)
    verify_written(OUTPUT_PATH, TIP)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
