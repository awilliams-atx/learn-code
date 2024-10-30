import itertools
from typing import Generator


def generate_seat_letters(number: int) -> Generator[str, None, None]:
    letter_cyler = itertools.cycle("ABCD")
    for _ in range(number):
        yield next(letter_cyler)


def generate_seats(seat_count: int) -> Generator[str, None, None]:
    letter_generator = generate_seat_letters(seat_count)
    row_numbers = (num for num in itertools.count(start=1) if num != 13)
    row_number = 0
    for _ in range(seat_count):
        letter = next(letter_generator)
        if letter == "A":
            row_number = next(row_numbers)
        yield f"{str(row_number)}{letter}"


def assign_seats(passengers: list[str]) -> dict[str, str]:
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(
    seat_numbers: list[str], flight_id: str
) -> Generator[str, None, None]:
    for number in seat_numbers:
        yield f"{number}{flight_id}".ljust(12, "0")
