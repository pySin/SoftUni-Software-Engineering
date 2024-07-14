# Truck Driver

# ⦁	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# ⦁	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]

season = input()  # "Spring", "Summer", "Autumn" или "Winter"
kilometers_per_month = float(input())
salary_four_season = 0

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        salary_four_season = (kilometers_per_month * 0.75) * 4
    elif 5000 < kilometers_per_month <= 10000:
        salary_four_season = (kilometers_per_month * 0.95) * 4
    elif 10000 < kilometers_per_month <= 20000:
        salary_four_season = (kilometers_per_month * 1.45) * 4
elif season == "Summer":
    if kilometers_per_month <= 5000:
        salary_four_season = (kilometers_per_month * 0.90) * 4
    elif 5000 < kilometers_per_month <= 10000:
        salary_four_season = (kilometers_per_month * 1.10) * 4
    elif 10000 < kilometers_per_month <= 20000:
        salary_four_season = (kilometers_per_month * 1.45) * 4
elif season == "Winter":
    if kilometers_per_month <= 5000:
        salary_four_season = (kilometers_per_month * 1.05) * 4
    elif 5000 < kilometers_per_month <= 10000:
        salary_four_season = (kilometers_per_month * 1.25) * 4
    elif 10000 < kilometers_per_month <= 20000:
        salary_four_season = (kilometers_per_month * 1.45) * 4

salary_four_season *= 0.90

print(f"{salary_four_season :.2f}")
