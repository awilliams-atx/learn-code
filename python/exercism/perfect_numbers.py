"""
https://exercism.org/tracks/python/exercises/perfect-numbers
"""


def classify(number: int) -> str:
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum([factor for factor in range(1, number) if number % factor == 0])
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum < number:
        return "deficient"
    return "abundant"
