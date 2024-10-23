# Do Pythonistas really use tuples like this? I don't know how to type
# a tuple of arbitrary length. I think a list is more appropriate.
# This is a useless function. There is no need to accept a variable number
# of ids and return them in a list. The caller can do this if it's needed.
def get_list_of_wagons(*ids):
    return list(ids)


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    y, z, a, *wagons = each_wagons_id
    return [a, *missing_wagons, *wagons, y, z]


def add_missing_stops(route, **stops):
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route: dict, more_route_information: dict) -> dict:
    return {**route, **more_route_information}


def fix_wagon_depot(wagon_rows):
    fixed = []
    for row in wagon_rows:
        for x, wagon in enumerate(row):
            if len(fixed) == x:
                fixed.append([])
            fixed[x].append(wagon)
    return fixed
