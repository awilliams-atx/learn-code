"""
https://exercism.org/tracks/python/exercises/anagram
Interestingly, sorting a short string to compare to the sorted target string
is faster than building a dictionary for each of the char counts. I guess
there could be a few reasons.

First, the dict building method. For each char:

    def get_char_counts(word):
        ret = {char: 0 for char in ascii_lowercase}
        for char in word:
            ret[char] += 1
        return ret

Setting the value in a dict takes only about 73% of the time it takes
to increment a value in a dict. Building the dict unfortunately includes
incrementing values:

    def set_keys():
        ret = {char: 0 for char in ascii_lowercase}
        for char in ascii_lowercase:
            ret[char] = 1
        return ret

    def inc_keys():
        ret = {char: 0 for char in ascii_lowercase}
        for char in ascii_lowercase:
            ret[char] += 1
        return ret

I suppose that get_char_counts() has to look up a dict char and then
set it equal to one plus the value it looked up.

Let's see if creating a dict is expensive compared to sorting a string
even if there's nothing in the dict.

    reversed_letters = reversed(string.ascii_lowercase)
    def sort_string():
        return sorted(reversed_letters)

    def make_dict():
        return {}

No. Making the empty dict takes 28% of the time it takes to sort the string.

What about setting each letter to a value of 0 in the dict?

    def make_dict():
        return {char: 0 for char in reversed_letters}

YES. That is slow. It is 83% of the sort time. Faster, but it doesn't actually
do any useful analysis on the string. In this algorithm, we sort the candidate
then compare it to the target (to exclude the candidate from the result list).

Now, how about comparing dicts vs comparing strings?

    dict_1 = {char: 1 for char in LETTERS}
    dict_2 = {char: 1 for char in LETTERS}

    def cmp_strs():
        return LETTERS == LETTERS

    def cmp_dicts():
        return dict_1 == dict_2

Not really a fair comparison, but it's a world of difference. Comparing the
strings takes 14% of the dict comparing time.

Actually, hold on. Python is doing some fancy short-circuiting on strings that
it doesn't do for dicts!

    short_str = ""
    long_str = string.ascii_lowercase * 1000
    small_dict = {}
    big_dict = {num: 1 for num in range(26_000)}


    def cmp_short_str():
        return short_str == short_str


    def cmp_long_str():
        return long_str == long_str


    def cmp_small_dict():
        return small_dict == small_dict


    def cmp_big_dict():
        return big_dict == big_dict

Comparing the same string to itself is not related to the length of the string.
Comparing dicts iterates through the keys even if you compare a dict to
itself.

How about building a dict and comparing it to another dict vs. sorting
a string and comparing it to another string?

    long_letters = sorted(ascii_lowercase * 100)
    reversed_letters = reversed(long_letters)
    dict_1 = {char: 1 for char in long_letters}

    def cmp_strs():
        return long_letters == sorted(reversed_letters)

    def cmp_dicts():
        return dict_1 == {char: 1 for char in long_letters}

AH. It is the BUILDING of the dict that is the slow part. Lookup in a dict
of this sort where there are only as many keys as there are letters in the
alphabet is much faster than comparing a string 100000 characters long.

    long_str = string.ascii_lowercase * 10000
    cmp_str = string.ascii_lowercase * 10000
    char_counts = {}
    cmp_counts = {}
    for char in string.ascii_lowercase:
        for counts in [char_counts, cmp_counts]:
            counts.setdefault(char, 0)
            counts[char] += 1


    def cmp_strs():
        return long_str == cmp_str


    def cmp_dict():
        return char_counts == cmp_counts

On a string 260_000 chars long, the dict is about 10 times faster here. As
the string grows shorter, string comparison takes the lead.

    26_000_000: chars: dict is 313x faster
    260_000: chars: dict is 12x faster
    26_000: chars: dict is 1.3x faster
    2_600: chars: str is 3x faster
    260: chars: str is 4.3x faster
    26: chars: str is 4.9x faster

That's as expected. Strings are just sequences of data, whereas dicts have a
more complex storage strategy. The constant lookup time of a dict is only
more performant than brute forcing your way through a list if the list is
sufficiently long. In this case, it appears that somewhere between 2_600 and
26_000 characters, the performance converges for this use case.

However, that doesn't matter if you have to build the dict. As demonstrated,
building a dict from a string is much slower than sorting the string.
"""


def find_anagrams(target: str, candidates: list[str]) -> list[str]:
    target = target.lower()
    target_sorted = sorted(target)
    length = len(target)
    anagrams = []
    for word in candidates:
        if len(word) != length:
            continue
        word_lower = word.lower()
        if word_lower == target:
            continue
        if sorted(word_lower) == target_sorted:
            anagrams.append(word)
    return anagrams
