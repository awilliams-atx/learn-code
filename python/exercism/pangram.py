"""
https://exercism.org/tracks/python/exercises/pangram
"""

import re

def is_pangram(sentence: str) -> bool:
    letters = re.sub(r"[^a-z]", "", sentence.lower())
    return len(set(letters)) == 26
