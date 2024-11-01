"""
https://exercism.org/tracks/python/exercises/house
I made some performance wins by building up the rhyme in a single string.
"""

LINES = [
    ("house that Jack built.", ""),
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
]


def recite(start: int, end: int) -> list[str]:
    segments = []
    for idx in range(0, end):
        who, what = LINES[idx]
        segments.append(who if idx == 0 else f"{who} that {what}")
    first_verse_idx = start - 1
    rhyme_ending = " the ".join(segments[first_verse_idx::-1])
    rhymes = []
    verse_indexes = range(first_verse_idx, len(segments))
    for verse_idx in verse_indexes:
        if verse_idx > first_verse_idx:
            rhyme_ending = f"{segments[verse_idx]} the {rhyme_ending}"
        rhymes.append(f"This is the {rhyme_ending}")
    return rhymes
