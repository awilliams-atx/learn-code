import re
import string


def response(hey_bob: str) -> str:
    hey_bob = hey_bob.rstrip()
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!" if hey_bob.isupper() else "Sure."
    return "Whoa, chill out!" if hey_bob.isupper() else "Whatever."
