from collections.abc import Iterable
from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: list[str]
) -> tuple[str, set[str]]:
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    has_alcohol = any(ingredient in ALCOHOLS for ingredient in drink_ingredients)
    return drink_name + (" Cocktail" if has_alcohol else " Mocktail")


CATEGORIES = [
    ("OMNIVORE", OMNIVORE),
    ("KETO", KETO),
    ("PALEO", PALEO),
    ("VEGETARIAN", VEGETARIAN),
    ("VEGAN", VEGAN),
]


def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    for category_name, category_ingredients in CATEGORIES:
        if category_ingredients.issuperset(dish_ingredients):
            return f"{dish_name}: {category_name}"
    raise RuntimeError("Could not find an appropriate dish category")


def tag_special_ingredients(dish: tuple[str, Iterable[str]]) -> tuple[str, set[str]]:
    dish_name, ingredients = dish
    return dish_name, SPECIAL_INGREDIENTS.intersection(ingredients)


def compile_ingredients(dishes: list[set[str]]) -> set[str]:
    return set.union(*dishes)


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: list[set[str]], intersection: set[str]) -> set[str]:
    return set.union(*dishes) - intersection
