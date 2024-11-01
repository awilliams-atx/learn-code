"""
https://exercism.org/tracks/python/exercises/rna-transcription
"""

TRANSLATION_TABLE = str.maketrans("GCTA", "CGAU")


def to_rna(dna: str) -> str:
    return dna.translate(TRANSLATION_TABLE)
