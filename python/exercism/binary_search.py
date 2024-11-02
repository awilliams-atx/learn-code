"""
https://exercism.org/tracks/python/exercises/binary-search
Binary search is such an intuitive algorithm but the implementation details
are always a tiny bit hard to get exactly right the first time. So here
are a few examples to understand the algorithm visually.

Below, bI represents the left and right bound index,
cI represents the midpoint between rI and lI, V represents the value at that
index, [<] and [>] represent continuing to the left or right

[1, 2, 3, 4, 5] -> 4
bI[0:4] I[2 == 0 + ((4 - 0) // 2)] V[3] [>]
bI[3:4] I[3 == 3 + ((4 - 3) // 2)] V[4]

[0, 1] -> -1
bI[0:1] I[0 == 0 + ((1 - 0) // 2)] V[0] [<]
bI[0:-1] V[Not in array]

Iteration seems to beat out recursion in Python3, but not by an order of
magnitude.
"""


def find(search_list: list[int], value: int) -> int:
    if len(search_list) == 0:
        raise ValueError("value not in array")
    left_idx = 0
    right_idx = len(search_list) - 1
    while True:
        idx = left_idx + (right_idx - left_idx) // 2
        candidate = search_list[idx]
        if candidate == value:
            return idx
        if left_idx >= right_idx:
            raise ValueError("value not in array")
        if candidate < value:
            left_idx = idx + 1
        else:
            right_idx = idx - 1
