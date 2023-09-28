# Fitness Card

# Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
# Пол - символ ('m' за мъж и 'f' за жена)
# Възраст - цяло число в интервала [5…105]
# Спорт - текст (една от възможностите в таблицата)

budget = float(input())
gender = input()  # m f
age = int(input())
sport = input()

amount_due = 0

if gender == "m":
    if sport == "Gym":
        amount_due = 42
    if sport == "Boxing":
        amount_due = 41
    if sport == "Yoga":
        amount_due = 45
    if sport == "Zumba":
        amount_due = 34
    if sport == "Dances":
        amount_due = 51
    if sport == "Pilates":
        amount_due = 39
elif gender == "f":
    if sport == "Gym":
        amount_due = 35
    if sport == "Boxing":
        amount_due = 37
    if sport == "Yoga":
        amount_due = 42
    if sport == "Zumba":
        amount_due = 31
    if sport == "Dances":
        amount_due = 53
    if sport == "Pilates":
        amount_due = 37

if age <= 19:
    amount_due *= 0.80

if amount_due <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${amount_due - budget :.2f} more.")
