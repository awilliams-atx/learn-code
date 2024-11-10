"""
https://exercism.org/tracks/python/exercises/protein-translation
"""

import itertools
import re
import textwrap
import timeit

# The data was given in this format
DATA_STR = """AUG	Methionine
UUU, UUC	Phenylalanine
UUA, UUG	Leucine
UCU, UCC, UCA, UCG	Serine
UAU, UAC	Tyrosine
UGU, UGC	Cysteine
UGG	Tryptophan
UAA, UAG, UGA	STOP
"""


def get_protein_by_codon(data: str) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for line in data.split("\n"):
        line_segments = re.split(r",?\s+", line)
        protein = line_segments[-1]
        for codon in line_segments[:-1]:
            lookup[codon] = protein
    return lookup


LOOKUP = get_protein_by_codon(DATA_STR)


def proteins(strand: str) -> list[str]:
    sequence: list[str] = []
    for idx in range(0, len(strand), 3):
        protein = LOOKUP[strand[idx : idx + 3]]
        if protein == "STOP":
            break
        sequence.append(protein)
    return sequence
