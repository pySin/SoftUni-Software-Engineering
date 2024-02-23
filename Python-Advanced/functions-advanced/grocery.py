# Grocery


def grocery_store(**kwargs):
    ordered_groceries = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    ordered_phrase = "\n".join([f"{item}: {quantity}" for item, quantity in ordered_groceries])
    return ordered_phrase


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
