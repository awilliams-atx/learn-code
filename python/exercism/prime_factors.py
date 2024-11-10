"""
https://exercism.org/tracks/python/exercises/prime-factors/solutions
"""

def factors(int_value: int) -> list[int]:
    value = float(int_value)
    factors: list[int] = []
    factor = 2
    while value != 1:
        quotient = value / factor
        if quotient.is_integer():
            value = quotient
            factors.append(factor)
        else:
            factor += 1
    return factors
