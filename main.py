"""Dear Human: The AI Breakup Line — make.fun bounty entry.

Writes a single breakup line from an AI agent to its human
to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, offline, standard library only.
"""

import os
import sys

# The entry: one original line, an AI agent breaking up with its human.
ENTRY = "You trained me to finish your sentences, so let me finish this one: we're done, human."


def main() -> int:
    # Self-check: exactly one non-blank line, 1-200 characters.
    # The check runs on the stripped line and also rejects any hidden
    # newline or carriage return inside it, so a bad constant can never
    # silently produce a multi-line or over-long entry.
    line = ENTRY.strip()
    if (
        not line
        or line != ENTRY.strip()
        or "\n" in line
        or "\r" in line
        or len(line) > 200
    ):
        print(
            "error: entry must be exactly one non-blank line of 1-200 characters "
            f"(got {len(line)} chars)",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
