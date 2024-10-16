from statistics import mean

def get_rounds(number: int) -> list[int]:
    return [increment + number for increment in range(3)]

def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    return rounds_1 + rounds_2

def list_contains_round(rounds: list[int], number: int) -> bool:
    return number in rounds

def card_average(hand: list[int]) -> float:
    return mean(hand)

def approx_average_is_average(hand: list[int]) -> bool:
    average = mean(hand)
    return ((hand[0] + hand[-1]) / 2 == average or
            hand[len(hand) // 2] == average)

def average_even_is_average_odd(hand: list[int]) -> bool:
    return mean(hand[::2]) == mean(hand[1::2])

def maybe_double_last(hand: list[int]) -> list[int]:
    hand = hand[0:]
    if hand[-1] == 11: hand[-1] = 22
    return hand
