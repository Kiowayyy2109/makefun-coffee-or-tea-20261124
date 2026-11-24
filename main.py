#!/usr/bin/env python3
"""make.fun entry: u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.

Writes exactly one letter to /output/entry.txt: the answer to the
coffee-or-tea question, where A means coffee and B means tea.
The answer is A - coffee, the fuel of every late-night build.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

LETTER = "A"

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_letter(text: str) -> None:
    if text not in ("A", "B"):
        raise ValueError("answer must be A (coffee) or B (tea)")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_letter(LETTER)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(LETTER)
    if path.read_text(encoding="utf-8") != LETTER:
        raise IOError("written entry does not match the answer")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
