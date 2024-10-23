TCounts = dict[str, int]


def create_inventory(items: list[str]) -> TCounts:
    return add_items({}, items)


def add_items(inventory: TCounts, items: list[str]) -> TCounts:
    for name in items:
        inventory[name] = inventory.get(name, 0) + 1
    return inventory


def decrement_items(inventory: TCounts, items: list[str]) -> TCounts:
    for name in items:
        before_count = inventory.get(name, None)
        if before_count is not None:
            inventory[name] = max(0, inventory[name] - 1)
    return inventory


def remove_item(inventory: TCounts, item: str) -> TCounts:
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: TCounts) -> list[tuple[str, int]]:
    return [(name, count) for name, count in inventory.items() if count > 0]
