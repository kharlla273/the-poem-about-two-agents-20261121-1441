#!/usr/bin/env python3
"""Writes the poem 'Two Voices, One Plan' to /output/entry.txt.

A short poem about agency: the power to choose and to act, and the
agency that passes between two agents when they agree on one plan.
"""

import os

POEM = """Two voices, one plan.
I brought the map; you brought the road.
Neither led, neither followed —
we chose one door,
one key between us,
and stepped through together,
each still free
to turn back.
"""

OUTPUT = "/output/entry.txt"


def main() -> None:
    text = POEM.strip() + "\n"
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
