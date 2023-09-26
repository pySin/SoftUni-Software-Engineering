# Cat Food

# На първи ред - броят на котките - цяло число в интервала [1..100]
# На всеки следващ ред за всяка котка - Х грама храна - реално число в интервала [100.00..400.00]

number_of_cats = int(input())

small_cats = 0
big_cats = 0
enormous_cats = 0

all_food = 0
days = 0

for _ in range(number_of_cats):

    food_grams = float(input())
    days += 1
    all_food += food_grams

    if 100 <= food_grams < 200:
        small_cats += 1
    elif 200 <= food_grams < 300:
        big_cats += 1
    elif 300 <= food_grams < 400:
        enormous_cats += 1

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {enormous_cats} cats.")

food_price_day = ((all_food / 1000) * 12.45)
print(f"Price for food per day: {food_price_day :.2f} lv.")
