"""
https://exercism.org/tracks/python/exercises/roman-n--umera-ls
I noticed after implementing this that it's simpler to hard-code
subtraction clusters like IX, XL, XC, etc. That's a better approach, I
think, since it reduces so much code at no performance cost. I'm leaving
mine like it is though without the hard-coding!
"""

from typing import NotRequired, TypedDict


class NumeralEnvironment(TypedDict):
    """
    The subtrahend is the only numeral/value that can be subcted
    from the upper numeral/value. For example, the lower and upper
    numerals/values for 90 are L/50 and C/100.  Only the largest power of
    ten lesser than the upper value is a valid subtrahend for that value--
    except I/1, which is a valid subtrahend for X/10. That means that 99
    cannot be IC. Instead, subtract 10 from the upper value then add
    whatever remains on the right side of the cluster:
    100 - 10 = 90 (XC); 9 = IX; 109 = XCIX
    """

    lower_n: str
    lower_v: int
    sub_n: NotRequired[str]
    sub_v: NotRequired[int]
    upper_n: NotRequired[str]
    upper_v: NotRequired[int]


NUMERALS = [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
]


def get_numeral_environment(value: int) -> NumeralEnvironment:
    first = None
    sub_pair = None
    for idx, pair in enumerate(NUMERALS):
        if pair[1] <= value:
            first = pair
            if idx % 2 == 0:
                sub_pair = pair
        elif first:
            assert sub_pair
            return {
                "lower_n": first[0],
                "lower_v": first[1],
                "sub_n": sub_pair[0],
                "sub_v": sub_pair[1],
                "upper_n": pair[0],
                "upper_v": pair[1],
            }
    assert first
    return {
        "lower_n": first[0],
        "lower_v": first[1],
    }


def roman(num: int) -> str:
    env = get_numeral_environment(num)
    lower_v = env["lower_v"]
    lower_n = env["lower_n"]
    if "sub_v" in env:
        assert "sub_n" in env and "upper_v" in env and "upper_n" in env
        upper_v = env["upper_v"]
        sub_val = env["sub_v"]
        if num >= upper_v - sub_val:
            remainder = num - upper_v + sub_val
            return (
                env["sub_n"] + env["upper_n"] + (roman(remainder) if remainder else "")
            )
    numeral_count = num // lower_v
    remainder = num - lower_v * numeral_count
    return lower_n * numeral_count + (roman(remainder) if remainder else "")
