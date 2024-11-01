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

    def cpm_dicts():
        return dict_1 == dict_2

Not really a fair comparison, but it's a world of difference. Comparing the
strings takes 14% of the dict comparing time.

How about building a dict and comparing it to another dict vs. sorting
a string and comparing it to another string?

    long_letters = sorted(ascii_lowercase * 100)
    reversed_letters = reversed(long_letters)
    dict_1 = {char: 1 for char in long_letters}

    def cmp_strs():
        return long_letters == sorted(reversed_letters)

    def cpm_dicts():
        return dict_1 == {char: 1 for char in long_letters}

I think the moral of the story is that look-up tables should be measured for
performance before automatically including them in algorithms.
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
