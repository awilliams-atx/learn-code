from math import sqrt

SCORES = [(1, 10), (5, 5), (10, 1)]


# This is slower than a series of conditionals checking the dart radius
# against the boundary. If performance is a concern, go with the conditionals.
def score(x: int, y: int) -> int:
    dart_radius = sqrt(x**2 + y**2)
    for score_radius, score in SCORES:
        if dart_radius <= score_radius:
            return score
    return 0
