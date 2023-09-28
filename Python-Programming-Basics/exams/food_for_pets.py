# Food For Pets

# ⦁	Брой дни – цяло число в диапазона [1…30]
# ⦁	Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# ⦁	Количество изядена храна от кучето – цяло число в диапазона [10…500]
# ⦁	Количество изядена храна от котката – цяло число в диапазона [10…500]

days_count = int(input())
food_available = float(input())

dog_food_amount = 0
cat_food_amount = 0
biscuits_amount = 0

for i in range(1, days_count + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())

    dog_food_amount += current_dog_food
    cat_food_amount += current_cat_food

    if i % 3 == 0:
        biscuits_amount += (current_dog_food + current_cat_food) * 0.10


all_food_amount = dog_food_amount + cat_food_amount

print(f"Total eaten biscuits: {int(biscuits_amount)}gr.")
print(f"{(all_food_amount / food_available) * 100 :.2f}% "
      f"of the food has been eaten.")
print(f"{(dog_food_amount / all_food_amount) * 100 :.2f}% eaten from the dog.")
print(f"{(cat_food_amount / all_food_amount) * 100 :.2f}% eaten from the cat.")
