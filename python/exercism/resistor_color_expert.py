"""
https://exercism.org/tracks/python/exercises/resistor-color-expert
"""

import re


def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1:
        return "0 ohms"
    num_str = "".join(str(LOOKUP[color]) for color in colors[:-2])
    multiplier_color, tolerance_color = colors[-2:]
    num_str += "0" * LOOKUP[multiplier_color]
    num_str = re.sub("^0*", "", num_str) or "0"
    length = len(num_str)
    extra_length = length - (length % 3)
    extra_length -= 3 if length % 3 == 0 else 0
    dot_idx = length - extra_length
    if dot_idx < length:
        post_dot = re.sub("0*$", "", num_str[dot_idx:])
        num_str = num_str[0:dot_idx] + (f".{post_dot}" if post_dot else "")
    prefix_idx = extra_length // 3 - 1
    return (
        f"{num_str} "
        + (prefix_idx >= 0 and PREFIXES[prefix_idx] or "")
        + "ohms "
        + f"±{TOLERANCES[tolerance_color]}%"
    )


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


TOLERANCES = {
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10",
}
