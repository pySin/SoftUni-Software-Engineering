# Easter Shop

# На първи ред - Началното количество яйца в магазина - цяло число в интервала [1… 10000]
# След това поредица от два реда (до получаване на команда "Close" или при заявка за купуване на повече от наличните в магазина яйца) :
# Команда за купуване или допълване на яйца в магазина – текст ("Buy" или "Fill")
# Брой на яйца, които да бъдат купени или допълнени в магазина – цяло число в интервала [1… 1000]

initial_amount_eggs = int(input())
eggs_sold = 0

eggs_amount = 0

while True:
    buy_or_fill = input()
    if buy_or_fill == "Close":
        print(f"Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    eggs_amount = int(input())

    if buy_or_fill == "Buy":
        initial_amount_eggs -= eggs_amount
        if initial_amount_eggs < 0:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {initial_amount_eggs + eggs_amount}.")
            break

        eggs_sold += eggs_amount

    elif buy_or_fill == "Fill":
        initial_amount_eggs += eggs_amount
