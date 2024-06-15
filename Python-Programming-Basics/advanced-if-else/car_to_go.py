# Car to go

# ⦁	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# ⦁	Втори ред –  Сезон – текст "Summer" или "Winter"

budget = float(input())
season = input()

rental_price = 0
class_car = ""
car_type = ""

if budget <= 100:
    car_type = "Cabrio"
    class_car = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        rental_price = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        rental_price = budget * 0.65
elif 100 < budget <= 500:
    # print("budget" + str(budget))
    class_car = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        rental_price = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        rental_price = budget * 0.80
elif budget > 500:
    class_car = "Luxury class"
    rental_price = budget * 0.90
    car_type = "Jeep"

print(f"{class_car}")
print(f"{car_type} - {rental_price :.2f}")
