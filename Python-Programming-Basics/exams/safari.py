# Safari

FUEL_PER_LITER = 2.10
GUIDE_PRICE = 100

# Бюджет – реално число в интервала [0.00… 10000.00]
# Колко литра гориво ще са им нужни – реално число в интервала [1.00… 50.00]
# Ден от седмицата – текст с възможности "Saturday" и "Sunday"

budget = float(input())
litres = float(input())
day_of_the_week = input()

fuel_bill = litres * FUEL_PER_LITER

full_bill = 0
if day_of_the_week == "Saturday":
    full_bill = (fuel_bill + GUIDE_PRICE) * (1 - 0.10)
    if full_bill <= budget:
        print(f"Safari time! Money left: {budget - full_bill :.2f} lv.")
    else:
        print(f"Not enough money! Money needed: {full_bill - budget :.2f} lv.")

else:
    full_bill = (fuel_bill + GUIDE_PRICE) * (1 - 0.20)
    if full_bill <= budget:
        print(f"Safari time! Money left: {budget - full_bill :.2f} lv. ")
    else:
        print(f"Not enough money! Money needed: {full_bill - budget :.2f} lv.")
