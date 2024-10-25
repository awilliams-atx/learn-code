# I can't import Self for some reason or the tests give an error
# We tried to import the 'Alien' class from your classes.py file, but could not find it
# from typing import Self
from typing import Any, Self


class Alien:
    total_aliens_created = 0

    def __init__(self, x: int, y: int) -> None:
        Alien.total_aliens_created += 1
        self.health = 3
        self.teleport(x, y)

    @classmethod
    def from_coordinate_pair(cls, pair: list[int]) -> Self:
        x, y = pair
        return cls(x, y)

    def collision_detection(self, other: Any) -> None:
        pass

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y


def new_aliens_collection(coordinate_pairs: list[list[int]]) -> list[Alien]:
    return list(map(Alien.from_coordinate_pair, coordinate_pairs))
