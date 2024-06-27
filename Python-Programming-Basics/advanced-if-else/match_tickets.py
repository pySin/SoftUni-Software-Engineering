# Match tickets

# ⦁	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# ⦁	На втория ред е категорията – "VIP" или "Normal"
# ⦁	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]

budget = float(input())
category = input() 
number_of_people = int(input())

transport_expenses = 0
tickets_expenses = 0

if category == "VIP":
    tickets_expenses = number_of_people * 499.99
if category == "Normal":
    tickets_expenses = number_of_people * 249.99

if 1 <= number_of_people <= 4:
    transport_expenses = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport_expenses = budget * 0.60
elif 10 <= number_of_people <= 24:
    transport_expenses = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport_expenses = budget * 0.40
elif number_of_people >= 50:
    transport_expenses = budget * 0.25

all_expenses = transport_expenses + tickets_expenses

if budget >= all_expenses:
    print(f"Yes! You have {budget - all_expenses :.2f} leva left.")
elif budget < all_expenses:
    print(f"Not enough money! You need {all_expenses - budget :.2f} leva.")
