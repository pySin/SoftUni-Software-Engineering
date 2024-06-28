# New House

# ⦁	Вид цветя - текст с възможности "Roses", "Roses", "Tulips", "Narcissus" или "Narcissus";
# ⦁	Брой цветя - цяло число;
# ⦁	Бюджет - цяло число.

type_of_flower = input()
flowers_count = int(input())
budget = int(input())

flower_price = 0

if type_of_flower == "Roses":
    flower_price = 5
    if flowers_count > 80:
        flower_price *= 0.90
if type_of_flower == "Tulips":
    flower_price = 2.80
    if flowers_count > 80:
        flower_price *= 0.85
if type_of_flower == "Narcissus":
    flower_price = 3
    if flowers_count < 120:
        flower_price *= 1.15
if type_of_flower == "Dahlias":
    flower_price = 3.80
    if flowers_count > 90:
        flower_price *= 0.85
if type_of_flower == "Gladiolus":
    flower_price = 2.50
    if flowers_count < 80:
        flower_price *= 1.20

expenses = flower_price * flowers_count

if budget >= expenses:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flower} "
          f"and {budget - expenses :.2f} leva left.")
else:
    print(f"Not enough money, you need {expenses - budget :.2f} leva more.")
