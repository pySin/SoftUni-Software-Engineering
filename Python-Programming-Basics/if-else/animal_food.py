# Animal Food
from math import floor, ceil

# Първи ред – брой дни – цяло число в интервал [1…5000]
# Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]

days = int(input())
all_food = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_gr = float(input())

all_dog_food = dog_food_per_day_kg * days
all_cat_food = cat_food_per_day_kg * days
all_turtle_food = (turtle_food_per_day_gr * days) / 1000

food_to_consume = all_dog_food + all_cat_food + all_turtle_food

if food_to_consume <= all_food:
    print(f"{floor(all_food - food_to_consume)} kilos of food left.")
else:
    print(f"{ceil(food_to_consume - all_food)} more kilos of food are needed.")
