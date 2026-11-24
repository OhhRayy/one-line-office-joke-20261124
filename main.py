"""The One-Line Office Joke (make.fun bounty u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162).

Writes a single office joke to /output/entry.txt. Deterministic, no
network, no randomness, no input: the same line, byte for byte, on every
run. The line was chosen for the judge's brief: a real one-line joke
about office life, a punchline that surprises and pays off a setup
anyone who has sat in an office recognises (asking HR for a raise),
a specific detail instead of a generic complaint (a mindfulness app
handed out in place of a raise), and tight wording — 87 characters,
one sentence, nothing left to explain.
"""

import os

LINE = (
    "I asked HR for a raise and they gave me a mindfulness app, "
    "so now I'm calmly underpaid."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. This line is 87 characters, one sentence.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    # Length is counted in Unicode code points (Python str length), not bytes.
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
