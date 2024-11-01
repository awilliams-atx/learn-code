"""
https://exercism.org/tracks/python/exercises/resistor-color-duo
"""

LOOKUP = {
    name: idx
    for idx, name in enumerate(
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


def value(colors: list[str]) -> int:
    return LOOKUP[colors[0]] * 10 + LOOKUP[colors[1]]
