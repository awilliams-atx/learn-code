"""
https://exercism.org/tracks/python/exercises/diamond
"""

A_ORD = ord("A")
SPACE = " "


def diamond(last_letter: str) -> list[str]:
    rows: list[str] = []
    row_width = (ord(last_letter) - A_ORD) * 2 + 1
    for code_point in range(A_ORD, ord(last_letter) + 1):
        char = chr(code_point)
        row = char
        code_point_difference = code_point - A_ORD
        if code_point_difference > 0:
            row = row + (SPACE * (code_point_difference * 2 - 1)) + char
        num_outside_dots = (row_width - len(row)) // 2
        rows.append((SPACE * num_outside_dots) + row + (SPACE * num_outside_dots))
    return rows if len(rows) == 1 else rows + rows[-2::-1]
