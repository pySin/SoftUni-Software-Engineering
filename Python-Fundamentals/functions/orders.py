# Orders

def orders(item, count):
    return {
        "coffee": 1.50 * count,
        "coke": 1.40 * count,
        "water": 1.00 * count,
        "snacks": 2.00 * count,
    }.get(item, "We don\'t sell this item!")


def check_int(sale_result):
    if sale_result != "We don\'t sell this item!":
        return f"{sale_result:.2f}"
    else:
        return sale_result


product = input()  # "coffee", "coke", "water", or "snacks"
quantity = int(input())

print(check_int(orders(product, quantity)))
