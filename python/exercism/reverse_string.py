"""
https://exercism.org/tracks/python/exercises/reverse-string
Reverse indexing a la text[::-1] is between 4 and 8 times faster
than building a string in a loop.
"""


def reverse(text: str) -> str:
    return text[::-1]
