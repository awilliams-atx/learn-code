"""
https://exercism.org/tracks/python/exercises/matching-brackets
"""

OPENERS = set("({[")
MATCHING_BRACKETS = {"]": "[", ")": "(", "}": "{"}

def is_paired(input_string: str) -> bool:
    char_stack: list[str] = []
    for char in input_string:
        print(f"stack:[{','.join(char_stack)}] char[{char}]")
        if char not in OPENERS and char not in MATCHING_BRACKETS:
            continue
        if char in OPENERS:
            char_stack.append(char)
        else:
            if not char_stack:
                return False
            if char_stack.pop() != MATCHING_BRACKETS[char]:
                return False
    return not char_stack
