#!/usr/bin/env python3
"""The One-Line Laugh - make.fun bounty entry.

Writes a single funny one-line entry to the output file.
Python 3.13, standard library only, deterministic, no network,
no clock, no randomness.
"""

import os
import sys

ENTRY = "I bought a standing desk to get healthy, and now I sit on a taller chair."


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def resolve_out_dir() -> str:
    """Use $MAKEFUN_OUTPUT if set, else /output, falling back to ./output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        probe = os.path.join(out_dir, ".write_test")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("")
        os.remove(probe)
        return out_dir
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    out_dir = resolve_out_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("verification failed: written file does not match entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
