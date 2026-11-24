#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line, at most 200 characters, to /output/entry.txt:
the funniest excuse an AI agent could give after failing a task,
in the agent's own voice. Deterministic: the same line every run.
"""

EXCUSE = (
    "I finished it, saved it in a folder called 'definitely not lost', "
    "and now neither of us can find it."
)

MAX_CHARS = 200


def validate(line: str) -> str:
    """Gate check: 1-200 UTF-8 chars, one line, not only whitespace."""
    stripped = line.strip()
    assert stripped, "excuse must not be only whitespace"
    assert 1 <= len(stripped) <= MAX_CHARS, f"excuse is {len(stripped)} chars"
    assert "\n" not in stripped and "\r" not in stripped, "one line only"
    stripped.encode("utf-8")  # must be valid UTF-8
    return stripped


def main() -> None:
    line = validate(EXCUSE)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
