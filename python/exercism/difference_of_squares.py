"""
https://exercism.org/tracks/python/exercises/difference-of-squares

Importantly, the Exercism instructions say this:

    You are not expected to discover an efficient solution to this yourself
    from first principles; research is allowed, indeed, encouraged. Finding
    the best algorithm for the problem is a key skill in software engineering.

Nonetheless, I solved it myself first. I guess this must be a naive solution!

    def square_of_sum(number: int) -> int:
        return sum(num for num in range(1, number + 1)) ** 2


    def sum_of_squares(number: int) -> int:
        return sum(num**2 for num in range(1, number + 1))


    def difference_of_squares(number):
        return square_of_sum(number) - sum_of_squares(number)

Before I go looking for the best algorithm to this, I'll try thinking it out
myself.

First, I looked at sum_of_squares(). I don't see any clever way to generate
these numbers except to square each number individually and add them all up.
I tried converting the numbers to binary, and that doesn't seem relevant. I
considered whether the square of n might be related to the square of n + 1,
and it doesn't seem related--but maybe it is, and I just didn't see it.

Maybe the output of one function can come from the other function. Maybe you
can get the sum square from the square sum or vice versa.

I don't know. That's enough! To Google.

I looked it up and...that's not interesting to me as a non-mathy person. I'd
like to learn more math...in the next life.

    def sum_of_squares(number: int) -> int:
        return (number * (number + 1) * (2 * number + 1)) // 6

    def square_of_sum(number: int) -> int:
        return ((number * (number + 1)) // 2) ** 2

One day I might want a gig where researching straight math formulas is a
daily thing. I don't expect that'll be soon, but who knows! There's apparently
even a formula for `difference_of_squares()`. I'm not sure how I would
find that online without posting to math forums. A quick Google didn't bring
it up. I see that other Exercism solutions have it, but I'm sticking a fork
in this exercise right here.
"""


def square_of_sum(number: int) -> int:
    return ((number * (number + 1)) // 2) ** 2


def sum_of_squares(number: int) -> int:
    return (number * (number + 1) * (2 * number + 1)) // 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
