"""
https://exercism.org/tracks/python/exercises/transpose
Using `zip_longest()` is a bit faster than the array approach, but it requires a
sentinel character since the solution must include spaces present in the
original string. E.g., the solution to "Single line." must include a line
which has a space " " between "single" and "line". Without a sentinel, this
would be stripped.

Sentinels are fine if you know that the sentinel won't be present in the
original string, but otherwise, they must be avoided unless a bit of error
is tolerable.
"""


def transpose(text: str) -> str:
    rows: list[list[str]] = []
    y = 0
    x = 0
    for char in text:
        if char == "\n":
            y = 0
            x += 1
            continue
        if len(rows) < y + 1:
            row: list[str] = []
            rows.append(row)
        else:
            row = rows[y]
        while len(row) < x:
            row.append(" ")
        row.append(char)
        y += 1
    return "\n".join(map(lambda row: "".join(row), rows))
