# Grocery List


def shop_from_grocery_list(budget: int, *args):
    kwargs = [kw for kw in args if type(kw) == tuple]
    args = [ar for ar in args if type(ar) == list][0]
    products_bought = []
    for product, price in kwargs:
        if budget < price:
            break
        if product in args and product not in products_bought:
            budget -= price
            products_bought.append(product)
        else:
            continue

    if len(products_bought) == len(args):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products = [product_ for product_ in args if product_ not in products_bought]
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
