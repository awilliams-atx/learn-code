"""
https://exercism.org/tracks/python/exercises/isogram
"""

import re

def is_isogram(word: str) -> bool:
    seen = set()
    for char in re.sub("[^a-z]", "", word.lower()):
        if char in seen:
            return False
        seen.add(char)
    return True
