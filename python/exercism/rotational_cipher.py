"""
https://exercism.org/tracks/python/exercises/rotational-cipher
"""

BOUNDS = [(ord(a), ord(b)) for a, b in [("A", "Z"), ("a", "z")]]


def get_bounds(code: int) -> tuple[int, int]:
    for bounds_pair in BOUNDS:
        start, end = bounds_pair
        if start <= code <= end:
            return bounds_pair
    raise ValueError("The code provided did not match a character between A-Z or a-z")


def rotate(text: str, key: int) -> str:
    out_chars = []
    for char in text:
        if not char.isalpha():
            out_chars.append(char)
            continue
        code = ord(char)
        start, end = get_bounds(code)
        code += key
        if not start <= code <= end:
            code += -26 if code > end else 26
        out_chars.append(chr(code))
    return "".join(out_chars)
