#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first that came to mind, to /output/entry.txt.
Nothing else: no punctuation, no newline, no second draft in the output.
"""

import os

WORD = "quiver"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
