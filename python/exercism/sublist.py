"""
https://exercism.org/tracks/python/exercises/sublist
"""

SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def check_from(start, one, two):
    if len(one) - start < len(two):
        return False
    for idx in range(start, start + len(two)):
        if one[idx] != two[idx - start]:
            return False
    return True


def sublist(one, two, last_try=False):
    if not one:
        return SUBLIST if two else EQUAL
    if not two:
        return SUPERLIST if one else EQUAL
    for idx in range(len(one)):
        if check_from(idx, one, two):
            return EQUAL if (len(one) == len(two)) else SUPERLIST
    if last_try:
        return UNEQUAL
    reverse_try = sublist(two, one, last_try=True)
    if reverse_try == UNEQUAL:
        return UNEQUAL
    return SUPERLIST if reverse_try == SUBLIST else SUBLIST
