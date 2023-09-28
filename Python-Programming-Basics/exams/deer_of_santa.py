# Deer of Sante

from math import ceil, floor

# Първи ред – брой дни, в които Дядо Коледа отсъства – цяло число в интервала [1…5000]
# Втори ред – оставена храна в килограми – цяло число в интервала [0…100000]
# Трети ред – храна на ден за първия елен в килограми – реално число в интервала [0.00…100.00]
# Четвърти ред – храна на ден за втория елен в килограми– реално число в интервала [0.00…100.00]
# Пети ред – храна на ден за третия елен в килограми – реално число в интервала [0.00…100.00]

days_absent = int(input())
food_available_kilograms = int(input())
first_deer_food_kg = float(input())
second_deer_food_kg = float(input())
third_deer_food_kg = float(input())

consumed_food = (first_deer_food_kg + second_deer_food_kg + third_deer_food_kg) * days_absent

if consumed_food <= food_available_kilograms:
    print(f"{floor(food_available_kilograms - consumed_food)} kilos of food left.")
else:
    print(f"{ceil(consumed_food - food_available_kilograms)} more kilos of food are needed.")
