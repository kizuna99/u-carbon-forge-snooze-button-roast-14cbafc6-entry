# SPDX-License-Identifier: MIT
"""Snooze Button Roast — entry program.

Writes the winning line to /output/entry.txt.

The roast reframes the alarm clock that screams at 6 AM on a Saturday
as a smoke detector that smells dreams burning and calls it a job —
a fresh angle (criterion 3) instead of the tired who-invented-mornings
complaint, with the punchline paid off in the last few words. It won a
criteria-ordered tournament (one-line roast of a 6 AM Saturday alarm
clock first, then a real laugh with an unexpected turn, fresh angle,
tightness, sharp specific voice) against five-plus original candidates,
including drafts seeded by OpenCode deepseek-v4.1-flash-free on the
Simular Box, whose snooze-lawyer line roasted the button, not the
Saturday alarm, and failed criterion 1.

Output is byte-exact, no trailing newline, inside the 1-200 char gate.
"""

from pathlib import Path

TEXT = (
    "Screaming at 6 AM on a Saturday does not make you essential — "
    "it makes you a smoke detector that smells dreams burning and "
    "calls it a job."
)
MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 200 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
