import re

VOWELS = "aeiou"


def translate(text: str) -> str:
    return " ".join(translate_word(x) for x in text.split(" "))


def translate_word(word: str) -> str:
    if any(word.startswith(x) for x in ["xr", "yt"]):
        return word + "ay"
    if re.match(f"^y[{VOWELS}]", word):
        return word[1:] + "yay"
    if re.match(f"^[{VOWELS}]", word):
        return word + "ay"
    match = re.match("^[bcdfghjklmnpqrstvwxz]+", word)
    assert match is not None
    start, stop = match.span()
    moveable = word[start:stop]
    if moveable.endswith("q") and word.startswith(moveable + "u"):
        moveable += "u"
    return word[len(moveable) :] + moveable + "ay"
