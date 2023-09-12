# Fuel Tank 2


# Бензин – 2.22 лева за един литър,
# Дизел – 2.33 лева за един литър
# Газ – 0.93 лева за литър

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

# Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# Количество гориво – реално число в интервала [1.00 … 50.00]
# Притежание на клубна карта – текст с възможности: "Yes" или "No"

fuel_type = input()
fuel_amount = float(input())
club_card = input()

if club_card == "Yes":
    fuel_type = fuel_type + "2"

fuel_bill = 0
if fuel_type == "Gasoline":
    fuel_bill = fuel_amount * GASOLINE
if fuel_type == "Gasoline2":
    fuel_bill = fuel_amount * (GASOLINE - 0.18)
elif fuel_type == "Diesel":
    fuel_bill = fuel_amount * DIESEL
elif fuel_type == "Diesel2":
    fuel_bill = fuel_amount * (DIESEL - 0.12)
elif fuel_type == "Gas":
    fuel_bill = fuel_amount * GAS
elif fuel_type == "Gas2":
    fuel_bill = fuel_amount * (GAS - 0.08)

if fuel_amount < 20:
    pass
elif fuel_amount > 25:
    fuel_bill *= 1 - 0.10
else:
    fuel_bill *= 1 - 0.08

print(f"{fuel_bill :.2f} lv.")

