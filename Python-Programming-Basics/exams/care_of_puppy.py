# Care of puppy

# Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда
# кученцето на всяко хранене - цяло число в интервала [10 …1000]

food_bought_kg = int(input())
food_bought_gr = food_bought_kg * 1000

food_grams_eaten = 0

while True:

    grams_eaten = input()

    if grams_eaten == "Adopted":
        break

    food_grams_eaten += int(grams_eaten)

if food_grams_eaten <= food_bought_gr:
    print(f"Food is enough! Leftovers: {food_bought_gr - food_grams_eaten} grams.")
else:
    print(f"Food is not enough. You need {food_grams_eaten - food_bought_gr} grams more.")
