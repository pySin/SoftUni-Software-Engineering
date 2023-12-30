# Computer Store


def prices_sum():

    command = input()
    amount_no_tax = 0

    while command != "special":

        if command == "regular":
            break

        product_price = float(command)
        if product_price < 0:
            print("Invalid price!")
            command = input()
            continue
        amount_no_tax += product_price

        command = input()

    return amount_no_tax, command


def calculate_final_price(price, client):
    taxes = price * 0.20
    if client == "regular":
        price *= 1.20
    elif client == "special":
        price *= 1.20
        price -= (price * 0.10)
    return price, taxes


def call_functions():
    no_tax_price, client_type = prices_sum()
    if no_tax_price == 0:
        print("Invalid order!")
    else:
        final_price, taxes = calculate_final_price(no_tax_price, client_type)

        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {no_tax_price :.2f}$")
        print(f"Taxes: {taxes :.2f}$")
        print("-----------")
        print(f"Total price: {final_price :.2f}$")


if __name__ == "__main__":
    call_functions()
