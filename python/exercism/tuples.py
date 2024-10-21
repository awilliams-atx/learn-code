from typing import Literal, NewType, Union


def get_coordinate(record: tuple[str, str]) -> str:
    return record[1]


def convert_coordinate(coordinate: str):
    return tuple(list(coordinate))


TAzara = NewType("TAzara", tuple[str, str])
TRui = NewType("TRui", tuple[str, tuple[str, str], str])
TCombined = NewType("TCombined", tuple[str, str, str, tuple[str, str], str])


def compare_records(azara_record: TAzara, rui_record: TRui) -> bool:
    return azara_record[1] == "".join(rui_record[1])


# If I return azara_record + rui_record, the tests pass, but Pyright reports
# the following:
# Type tuple[str | tuple[str, str], ...] is not assignable to return type
# "TCombined | Literal['not a match']"


def create_record(
    azara_record: TAzara,
    rui_record: TRui,
):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    return "".join(
        [
            str(tuple(rec[index] for index in [0, 2, 3, 4])) + "\n"
            for rec in combined_record_group
        ]
    )
