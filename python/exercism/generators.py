"""
https://exercism.org/tracks/python/exercises/plane-tickets
"""

import itertools
from typing import Generator

LETTERS = "ABCD"


def generate_seat_letters(number: int) -> Generator[str, None, None]:
    yield from itertools.islice(itertools.cycle(LETTERS), number)


def generate_seats(seat_count: int) -> Generator[str, None, None]:
    yield from itertools.islice(
        (
            f"{row_number}{letter}"
            for row_number in itertools.count(1)
            for letter in LETTERS
            if row_number != 13
        ),
        seat_count,
    )


def assign_seats(passengers: list[str]) -> dict[str, str]:
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(
    seat_numbers: list[str], flight_id: str
) -> Generator[str, None, None]:
    yield from map(
        lambda num: f"{num}{flight_id}".ljust(12, "0"),
        seat_numbers,
    )
