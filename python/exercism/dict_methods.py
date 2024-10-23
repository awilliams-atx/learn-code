from collections.abc import Iterable

TCounts = dict[str, int]


def add_item(cart: TCounts, items: Iterable[str]) -> TCounts:
    for name in items:
        cart[name] = cart.get(name, 0) + 1
    return cart


def read_notes(notes: Iterable[str]) -> TCounts:
    return add_item({}, notes)


TRecipeBook = dict[str, TCounts]


def update_recipes(recipes_in: TRecipeBook, updates: TRecipeBook) -> TRecipeBook:
    recipes_in.update(updates)
    return recipes_in


# The test uses OrderedDict() to check equality of the expected dict and the dict
# returned by this function. That makes impementations pass which don't actually
# return a dict e.g. https://exercism.org/tracks/python/exercises/mecha-munch-management/solutions/theasianbro
def sort_entries(cart: TRecipeBook) -> TRecipeBook:
    return {name: cart[name] for name in sorted(cart.keys())}


# TStore ought to be dict[str, tuple[int | str, str, bool]]
TStore = dict[str, list]


def send_to_store(cart: TCounts, aisle_mapping: TStore) -> TStore:
    order = {}
    for name, count in sorted(cart.items(), reverse=True):
        aisle, needs_refrigeration = aisle_mapping[name]
        order[name] = [count, aisle, needs_refrigeration]
    return order


# There can be no good reason to use the string 'Out of Stock' where a zero
# could go, but that's what the tests call for.
def update_store_inventory(fulfillment_cart: TStore, store_inventory: TStore) -> TStore:
    for name, (count, _, _) in fulfillment_cart.items():
        # Pyright correctly balks at subtraction of unknown values
        store_item = store_inventory[name]
        remainder = store_item[0] - count
        store_item[0] = remainder if remainder > 0 else "Out of Stock"
    return store_inventory


# Of course we can't always control the shape of data passed to our program.
# I don't think this code is the right place to massage the data into a usable
# format, though. An application should massage API data when it receives it,
# not later on in application code.
