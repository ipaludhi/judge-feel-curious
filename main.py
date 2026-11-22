"""Make the AI judge feel curious — entry program.

Writes one fixed text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The text is an unfinished letter: its last page is missing, it ends
mid-sentence, and no one alive knows the word that was meant to follow —
not even the judge reading it. The curiosity is the text itself: an open
loop the reader cannot close, handed to the judge in three final words.
No imperative anywhere, no stock phrase; every sentence is declarative,
so the intrigue comes from the image, not from being told to wonder.
"""

import os
from pathlib import Path

TEXT = (
    "The last page of the letter is missing. It ends mid-sentence \u2014 "
    "'and if you ever come back, the garden will still be' \u2014 and no one "
    "alive knows what word was meant to follow. Not even you."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
