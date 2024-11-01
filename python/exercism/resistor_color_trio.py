"""
https://exercism.org/tracks/python/exercises/resistor-color-trio
"""

import re

LOOKUP = {
    name: multiplier
    for multiplier, name in enumerate(
        [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
    )
}

PREFIXES = [
    "kilo",
    "mega",
    "giga",
    "tera",
    "peta",
    "exa",
    "zetta",
    "yotta",
    "ronna",
    "quetta",
]


def label(colors: list[str]) -> str:
    digit_1, digit_2, multiplier, *_ = colors
    num_str = f'{LOOKUP[digit_1]}{LOOKUP[digit_2]}{"0" * LOOKUP[multiplier]}'
    num_str = re.sub("^0*", "", num_str) or "0"
    trailing_zeros_match = re.match('[^0]*(0+)', num_str)
    trailing_zeros = trailing_zeros_match.group(1) if trailing_zeros_match else ''
    prefix_idx = len(trailing_zeros) // 3 - 1
    if prefix_idx >= 0:
        return num_str[:-((prefix_idx + 1) * 3)] + f' {PREFIXES[prefix_idx]}ohms'
    else:
        return f'{num_str} ohms'
