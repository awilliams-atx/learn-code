"""
https://exercism.org/tracks/python/exercises/say
"""

SEGMENT_NAMES = [None, "thousand", "million", "billion"]
ONES = [
    "ERROR",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
TEENS = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS = [
    "ERROR",
    "ERROR",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def say_segment(num: int) -> str:
    "Spell out a number between 1 and 999 in English"
    words: list[str] = []
    if num >= 100:
        words.append(f"{ONES[num // 100]} hundred")
    num %= 100
    num_tens = num // 10
    tens_word = None
    if num_tens == 1:
        words.append(TEENS[num - 10])
        num = 0
    elif num_tens > 1:
        tens_word = TENS[num_tens]
    num %= 10
    if num == 0 and tens_word:
        words.append(tens_word)
    elif num > 0:
        ones_word = ONES[num]
        words.append((f"{tens_word}-" if tens_word else "") + ones_word)
        tens_word = None
    return " ".join(words)


MAX_NUMBER = 999_999_999_999


def say(number: int) -> str:
    "Spell out a number between 0 and 1e12 - 1 in English"
    if 0 > number or number > MAX_NUMBER:
        raise ValueError("input out of range")
    digits = str(number)
    segments: list[str] = []
    for segment_name, segment in zip(
        SEGMENT_NAMES,
        [digits[max(0, idx - 3) : idx] for idx in range(len(digits), 0, -3)],
    ):
        if segment.replace("0", "") == "":
            continue
        segments.append(
            say_segment(int(segment)) + (f" {segment_name}" if segment_name else "")
        )
    return " ".join(reversed(segments)) if segments else "zero"
