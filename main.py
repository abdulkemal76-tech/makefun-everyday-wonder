"""Everyday Wonder entry.

Writes one sentence to /output/entry.txt: a small everyday moment
made strange and new.
"""

import os

SENTENCE = (
    "The fridge hums all night, and at dawn you realise it has been "
    "keeping time with your breathing since the day you moved in."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
