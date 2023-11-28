# Statistics

def statistics():

    command = input()
    stock = {}

    while command != "statistics":

        receive_stock = command.split(": ")
        if receive_stock[0] in stock.keys():
            stock[receive_stock[0]] += int(receive_stock[1])
        else:
            stock[receive_stock[0]] = int(receive_stock[1])
        command = input()

    return stock


get_statistics = statistics()
print("Products in stock:")
total_products = 0
total_quantity = 0
for key, value in get_statistics.items():
    total_products += 1
    total_quantity += value
    print(f"- {key}: {value}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
