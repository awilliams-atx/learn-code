"""
https://exercism.org/tracks/python/exercises/isbn-verifier
"""


def is_valid(isbn: str) -> bool:
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    for idx, char in enumerate(isbn):
        if char == "X":
            if idx != 9:
                return False
            total += 10
        elif str.isnumeric(char):
            total += int(char) * (10 - idx)
        else:
            return False
    return total % 11 == 0
