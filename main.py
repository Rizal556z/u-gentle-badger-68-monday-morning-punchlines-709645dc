#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun Growth entry.

Writes a single joke about Monday mornings to /output/entry.txt.
Pure Python standard library only.
"""

import os

JOKE = (
    "My alarm went off Monday morning and my bed counter-offered: "
    "a raise, free naps, no meetings. I still had to leave it for work."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the written file matches exactly (no trailing
    # newline, single line, within the 1-200 char gate).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry does not match the joke"
    assert "\n" not in written and 1 <= len(written) <= 200
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
