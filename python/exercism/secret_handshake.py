"""
https://exercism.org/tracks/python/exercises/secret-handshake
I've always thought binary operations were too magical to learn.
Exercism to the rescue!

NOTE: The instructions say to reverse if the first bit is 1, but
I didn't want to traverse the bits right to left since I'm working
with a string of bits instead of actual binary. My actions lookup
is reversed instead.

There are more binary exercises...
https://exercism.org/tracks/python/exercises/grains
I already completed that one but I guess I need to go back and solve it
binari-ly.
https://exercism.org/tracks/python/exercises/eliuds-eggs
https://exercism.org/tracks/python/exercises/Allergies
I haven't got to these two yet.
"""

LOOKUP = ["jump", "close your eyes", "double blink", "wink"]


def commands(binary: str) -> list[str]:
    length = len(binary)
    should_reverse = length == 5 and binary[0] == "0"
    actions = [
        LOOKUP[idx]
        for idx, bit in enumerate(binary if length < 5 else binary[1:])
        if bit == "1"
    ]
    return list(reversed(actions)) if should_reverse else actions
