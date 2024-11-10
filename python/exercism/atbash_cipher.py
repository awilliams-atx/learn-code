"""
https://exercism.org/tracks/python/exercises/atbash-cipher
Python's string method `translate` is very fast!
"""

from string import ascii_lowercase

CIPHER_TABLE = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(text: str) -> str:
    result = "".join(char for char in text.lower() if char.isalnum()).translate(
        CIPHER_TABLE
    )
    return " ".join(result[idx : idx + 5] for idx in range(0, len(result), 5))


def decode(text: str) -> str:
    return text.replace(" ", "").translate(CIPHER_TABLE)
