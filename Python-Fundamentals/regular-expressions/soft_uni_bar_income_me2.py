# Soft Uni Bar Income
import re


def order_validate(order):
    pattern = r"%([A-Z][a-z]+)%[^|$%\.]*<(\w+)>[^|$%\.]*\|([0-9]+)\|[^|$%\.0-9]*([0-9]+[\.]{0,1}[0-9]*)\$"
    # pattern = r"%([A-Z][a-z]+)%[^|$%\.]*<([A-Z][a-z]+)>[^|$%\.]*\|([0-9]+)\|[^|$%\.0-9]*([0-9\.]+)\$"
    result = re.search(pattern, order)
    if result:
        name, product, quantity, price = result.groups()
        client_checkout = int(quantity) * float(price)
        print(f"{name}: {product} - {client_checkout:.2f}")
        return client_checkout
    else:
        return 0


def receive_orders():
    total_income = 0

    command = input()
    while command != "end of shift":

        total_income += order_validate(command)

        command = input()
    print(f"Total income: {total_income:.2f}")


def function_call():
    receive_orders()


if __name__ == "__main__":
    function_call()
