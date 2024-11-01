"""
https://exercism.org/tracks/python/exercises/resistor-color
"""

COLORS = [
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

LOOKUP = {name: idx for idx, name in enumerate(COLORS)}


def color_code(color: str) -> int:
    return LOOKUP[color]


def colors():
    return COLORS
