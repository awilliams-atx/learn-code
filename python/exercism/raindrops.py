def convert(number: int) -> str:
    rain_sound = ""
    pairs = [(3, "i"), (5, "a"), (7, "o")]
    for divisor, vowel in pairs:
        if number % divisor == 0:
            rain_sound += f"Pl{vowel}ng"
    return rain_sound or str(number)
