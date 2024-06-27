# Journey

# ⦁	Бюджет - реално число;
# ⦁	Един от двата възможни сезона - "summer” или "winter”.

budget = float(input())
season = input()

destination = ""
expenses = 0
accommodation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        expenses = budget * 0.30
    elif season == "winter":
        accommodation = "Hotel"
        expenses = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        expenses = budget * 0.40
    elif season == "winter":
        accommodation = "Hotel"
        expenses = budget * 0.80
elif budget > 1000:
    accommodation = "Hotel"
    destination = "Europe"
    expenses = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{accommodation} - {expenses :.2f}")
