#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

A dark lord before the gates at dawn, postponing his own apocalypse.
The tiredness is never stated -- it lives in the deferrals.
"""

import os

MONOLOGUE = (
    "Sound the horns at dawn, I said. Well. Let the sun climb a bit first. "
    "A dark lord does not squint. I burned the nine libraries of Avelmere. "
    "I taught the dead to march in step, and kings to whisper my name. "
    "This city will kneel -- after the horns. "
    "Why are the horns not -- no, wait. Let them wait. Fear ripens. Do not hover, herald. "
    "Bring my chair. A throne is a chair that learned patience. "
    "When I was young I razed three kingdoms before breakfast. Three. "
    "Now the gates can hold till noon. In the end, everything falls. "
    "Mostly when I sit down."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    print(f"wrote {path}: {len(MONOLOGUE)} chars, {len(MONOLOGUE.split())} words")


if __name__ == "__main__":
    main()
