# Orders


def orders():

    command = input()
    products_information = {}

    while command != "buy":

        delivery = command.split()

        product_name = delivery[0]
        price = float(delivery[1])
        quantity = int(delivery[2])

        if product_name not in products_information.keys():
            products_information[product_name] = [quantity, price]
        elif product_name in products_information.keys():
            products_information[product_name][0] += quantity
            products_information[product_name][1] = price

        command = input()

    return products_information


if __name__ == "__main__":
    for key, value in orders().items():
        total_price = value[0] * value[1]
        print(f"{key} -> {total_price:.2f}")
