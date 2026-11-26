#!/usr/bin/env python3
"""make.fun entry: Worst Superpower (worst-superpower-b).

The entry is one line inventing the most useless superpower,
written to /output/entry.txt: the power to know exactly when
the Wi-Fi will die — three seconds after it already has. It is
a real power (perfectly accurate, never wrong) and perfectly
worthless, because the information always arrives too late to
use. A superpower whose only function is hindsight is the whole
joke in one line.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 140


def build_entry():
    """Return the superpower line, my own wording throughout."""
    # The structure is a promise followed by a betrayal: "know
    # exactly when" sounds useful, and "three seconds after it
    # already has" cancels it. The Wi-Fi dying is the universal
    # version of the power — everyone has lived the moment.
    return (
        "The power to know exactly when the Wi-Fi will die \u2014 "
        "three seconds after it already has."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
