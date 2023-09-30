# Tourist Shop

# На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# След това поредица от два реда (до получаване на команда "Stop" или при заявка за
# купуване на продукт, чиято стойност е по-висока от наличния бюджет) :
# Име на продукта – текст
# Цена на продукта – реално число в интервала [1.00… 5000.00]

budget = float(input())
bill = 0

amount = 0
while True:
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {amount} products for {bill :.2f} leva.")
        break

    amount += 1
    product_price = float(input())
    if amount % 3 == 0:
        product_price *= 0.50
    bill += product_price

    if bill > budget:
        print("You don't have enough money!")
        print(f"You need {bill - budget :.2f} leva!")
        break
