# Easter Decoration

# Брои на клиентите в магазина – цяло число [1… 100]
# След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")

number_of_clients = int(input())
income = 0

x = 0
while x < number_of_clients:
    x += 1

    number_of_items = 0
    client_bill = 0
    while True:
        purchase = input()

        if purchase == "Finish":
            if number_of_items % 2 == 0:
                client_bill *= 0.80
            print(f"You purchased {number_of_items} items for {client_bill :.2f} leva.")
            break
        elif purchase == "basket":
            number_of_items += 1
            client_bill += 1.50
        elif purchase == "wreath":
            number_of_items += 1
            client_bill += 3.80
        elif purchase == "chocolate bunny":
            number_of_items += 1
            client_bill += 7

    income += client_bill


average_bill = income / number_of_clients
print(f"Average bill per client is: {average_bill :.2f} leva.")
