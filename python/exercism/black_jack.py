"""
Blackjack related learning exercise for Python
"""

from __future__ import annotations

FACE_CARDS = {'J', 'Q', 'K'}

def value_of_card(card: str) -> int:
    if card in FACE_CARDS:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value > card_two_value:
        return card_one
    if card_one_value < card_two_value:
        return card_two
    return card_one, card_two

def value_of_ace(card_one: str, card_two: str) -> int:
    if 'A' in (card_one, card_two):
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    return 1


VAL_10_CARDS = set(FACE_CARDS)
VAL_10_CARDS.add('10')

def is_blackjack(card_one: str, card_two: str) -> bool:
    hand = {card_one, card_two}
    return 'A' in hand and len(VAL_10_CARDS.intersection(hand)) > 0


def can_split_pairs(card_one, card_two) -> bool:
    return (card_one == card_two or
            {card_one, card_two}.issubset(VAL_10_CARDS))


def can_double_down(card_one: str, card_two: str) -> bool:
    hand_value = value_of_card(card_one) + value_of_card(card_two)
    return 8 < hand_value < 12
