# Excursion Calculator

# Първи ред – брой хора – цяло число в интервала [1 … 20]
# Втори ред – сезон – текст с възможности - "spring", "summer", "autumn" или "winter"

number_of_people = int(input())
season = input()

holiday_price = 0

if season == "spring":
    if number_of_people <= 5:
        holiday_price = number_of_people * 50.00
    elif number_of_people > 5:
        holiday_price = number_of_people * 48.00
elif season == "summer":
    if number_of_people <= 5:
        holiday_price = number_of_people * 48.50
    elif number_of_people > 5:
        holiday_price = number_of_people * 45.00
elif season == "autumn":
    if number_of_people <= 5:
        holiday_price = number_of_people * 60.0
    elif number_of_people > 5:
        holiday_price = number_of_people * 49.50
elif season == "winter":
    if number_of_people <= 5:
        holiday_price = number_of_people * 86.0
    elif number_of_people > 5:
        holiday_price = number_of_people * 85.00

if season == "summer":
    holiday_price *= 0.85
elif season == "winter":
    holiday_price *= 1.08

print(f"{holiday_price :.2f} leva.")
