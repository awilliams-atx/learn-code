import functools
import math


def round_scores(student_scores: list[float]) -> list[int]:
    return [round(num) for num in student_scores]


def my_round(num: float) -> int:
    modulus = num % 1
    return math.floor(num) if modulus < 0.5 else math.ceil(num)


def count_failed_students(student_scores: list[int]) -> int:
    return functools.reduce(
        lambda count, score: count if score > 40 else count + 1, student_scores, 0
    )


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    return [num for num in student_scores if num >= threshold]


def letter_grades(highest: int) -> list[int]:
    spread = (highest - 40) // 4
    return [41 + spread * factor for factor in range(4)]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    return [
        f"{idx + 1}. {name}: {score}"
        for idx, (name, score) in enumerate(zip(student_names, student_scores))
    ]


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []
