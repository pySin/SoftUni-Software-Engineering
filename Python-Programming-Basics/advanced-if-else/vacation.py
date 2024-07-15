# Vacation

# ⦁	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# ⦁	Втори ред –  Сезон – текст "Summer" или "Winter"

budget = float(input())
season = input()

accommodation = ""
destination = ""
stay_price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        stay_price = budget * 0.65
    elif season == "Winter":
        destination = "Morocco"
        stay_price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        stay_price = budget * 0.80
    elif season == "Winter":
        destination = "Morocco"
        stay_price = budget * 0.60
if budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        stay_price = budget * 0.90
    elif season == "Winter":
        destination = "Morocco"
        stay_price = budget * 0.90

print(f"{destination} - {accommodation} - {stay_price :.2f}")
