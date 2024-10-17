def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
) -> list[str]:
    queue = express_queue if ticket_type == 1 else normal_queue
    queue.append(person_name)
    return queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    return sorted(queue)
