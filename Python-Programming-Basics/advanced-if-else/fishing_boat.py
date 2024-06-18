# Fishing Boat


budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter"
fishers = int(input())

ship_hire_price = 0

if season == "Spring":
    ship_hire_price = 3000
    if fishers <= 6:
        ship_hire_price *= 0.90
    elif 6 < fishers <= 11:
        ship_hire_price *= 0.85
    elif fishers > 12:
        ship_hire_price *= 0.75

    if fishers % 2 == 0:
        ship_hire_price *= 0.95
if season == "Summer" or season == "Autumn":
    ship_hire_price = 4200
    if fishers <= 6:
        ship_hire_price *= 0.90
    elif 6 < fishers <= 11:
        ship_hire_price *= 0.85
    elif fishers > 12:
        ship_hire_price *= 0.75

    if fishers % 2 == 0 and season != "Autumn":
        ship_hire_price *= 0.95

if season == "Winter":
    ship_hire_price = 2600
    if fishers <= 6:
        ship_hire_price *= 0.90
    elif 6 > fishers <= 11:
        ship_hire_price *= 0.85
    elif fishers > 12:
        ship_hire_price *= 0.75

    if fishers % 2 == 0:
        ship_hire_price *= 0.95

if budget >= ship_hire_price:
    print(f"Yes! You have {budget - ship_hire_price :.2f} leva left.")
else:
    print(f"Not enough money! You need {ship_hire_price - budget :.2f} leva.")
