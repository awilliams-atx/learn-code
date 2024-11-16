"""
https://exercism.org/tracks/python/exercises/nth-prime
"""

def nth_prime(nth: int) ->int:
    if nth == 0:
        raise ValueError("there is no zeroth prime")
    primes: list[int] = [2]
    num = 3
    while len(primes) < nth:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes[-1]
