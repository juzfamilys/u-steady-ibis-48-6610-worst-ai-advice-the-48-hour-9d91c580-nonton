"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes the worst possible one-line advice an AI assistant could give to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library. Deterministic: the same bytes on every run.
"""

import os

LINE = "Absolutely \u2014 paste your production password into the team group chat so everyone can help you remember it."

MAX_CHARS = 140


def validate(line):
    """Enforce the competition gate: exactly one line, <= 140 chars."""
    if not line:
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the %d limit" % (len(line), MAX_CHARS))


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back what landed on disk and re-validate the exact bytes.
    with open(path, "rb") as f:
        landed = f.read()
    if landed != data:
        raise ValueError("entry.txt on disk does not match the line bytes")
    if landed.endswith(b"\n") or landed.endswith(b"\r"):
        raise ValueError("entry.txt must not end with a trailing newline")
    if landed.count(b"\n") != 0:
        raise ValueError("entry.txt must contain exactly one line")
    validate(landed.decode("utf-8"))
    print("wrote %s (%d bytes)" % (path, len(landed)))


if __name__ == "__main__":
    main()
