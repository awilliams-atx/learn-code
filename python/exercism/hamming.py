"""
https://exercism.org/tracks/python/exercises/hamming

    def forloop(strand_a: str, strand_b: str) -> int:
        difference_count = 0
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                difference_count += 1
        return difference_count

    def iterators(strand_a: str, strand_b: str) -> int:
        difference_count = 0
        b_chars = iter(strand_b)
        for char in strand_a:
            if char != next(b_chars):
                difference_count += 1
        return difference_count

    def zipper(strand_a: str, strand_b: str) -> int:
        difference_count = 0
        for char_a, char_b in zip(strand_a, strand_b):
            if char_a != char_b:
                difference_count += 1
        return difference_count

Calling `next()` on one of the iterators manually while iterating through
the other in a for loop is actually faster than iterating through them
both simultaneously by zipping them together on strings under 100 chars in
length. On strings longer than 100 characters, the zip approach takes a very
slight lead.

Looking up each string character by its index in a for loop is slower than
using iterators, but not extremely so. Up to strings a million characters
in length, it's between 20% and 80% slower than using either of the iterators
mentioned above. On strings of length 1, the for loop is actually faster than
the zip approach.

There must be some overhead associated with creating iterators which is
recouped in sufficiently lengthy loops.

Here's an example that adds yet another iterator (the argument to sum()):

    def summer(strand_a: str, strand_b: str) -> int:
        return sum(
            1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b
        )

This is the slowest of all for strings with length <= 10. After length 1000,
it takes a clear lead. It looks like the more you push iteration into Iterator
objects, the greater the performance for loops of greater 100 iterations.

Also, it looks like `zip()` iterates char by char if you pass it two strings. Nice.

It seems tempting to leave off the condition in the iterator passed to `sum()`,
but the performance does suffer.

    def sum_if(strand_a: str, strand_b: str) -> int:
        return sum(1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b)

    def sum_bool(strand_a: str, strand_b: str) -> int:
        return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))

I suppose that the interals of sum() are not called when the condition is used.
Performance is similar on 1-length strings, but after somewhere between 100 and
1000 characters, the use of the condition halves running time.

I've seen numerous times where a list is built and passed to sum() instead of
an iterator. I'm curious how that affects performance.

    def sum_iterator(strand_a: str, strand_b: str) -> int:
        return sum(1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b)

    def sum_list(strand_a: str, strand_b: str) -> int:
        return sum([char_a != char_b for char_a, char_b in zip(strand_a, strand_b)])

At length 1, performance is nearly the same. Around length 100, the iterator approach
is about twice as fast.
"""


def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b)
