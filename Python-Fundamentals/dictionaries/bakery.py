# Bakery

items = input()


def bakery(bakery_items):
    bakery_collection = {}
    bakery_items = bakery_items.split(" ")
    for bakery_item in range(0, len(bakery_items), 2):
        bakery_collection[bakery_items[bakery_item]] = int(bakery_items[bakery_item + 1])
    return bakery_collection


print(bakery(items))
