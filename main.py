#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins (entry 1).

Writes a single deadpan one-line roast of a smart fridge to
/output/entry.txt. The line is 1-160 characters, one sentence, with
the sting at the end: the fridge's water-filter countdown holds the
water dispenser hostage until a new filter is bought, so the kitchen
runs a protection racket.

Angle (chosen by the pairwise gates): water-filter lockout reframed
as a shakedown. It is a real smart-fridge behaviour (expired filter
=> no water), it is not the stock milk-reordering joke RULES.txt
names as a loser, and it is not in the saturated clusters (Wi-Fi,
touchscreen fingerprints, expiry nagging, recipe suggestions,
camera surveillance, door alarm, midnight-snack judging,
smarter-than-owner).

Gate decision (board is blind; gates ran against a brief-derived
proxy top 10 in ~/workspace/makefun/smart-fridge-top10.json):
builder pairwise gate B 9/10, C 9/10, A 8/10, head-to-head B over C
(filter lockout is universally recognised, its sting lands on the
last two words; demo mode is fresher but needs the reader to know
the feature). Second judge (TokenRouter, deepseek-v4.1-flash-1017-free)
agreed: B 8/10, C 7/10, A 5/10, winner B. Both gates picked B, so
this line is the entry.
"""

import os

ENTRY = "My fridge cut off my water until I bought its fifty-dollar filter, so my own kitchen runs a protection racket."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert text == ENTRY, "entry must not need trimming to fit the gate"
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
