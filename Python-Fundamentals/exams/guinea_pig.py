# Guinea pig


food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000

guinea_pig_weight = float(input()) * 1000
month = 30

is_pet_support_finished = False
for i in range(1, 30 + 1):

    food -= 300

    if i % 2 == 0:
        percent_5_of_food_left = food * 0.05
        hay -= percent_5_of_food_left

    if i % 3 == 0:
        third_of_puppy_weight = guinea_pig_weight / 3
        cover -= third_of_puppy_weight

    if food <= 0 or hay <= 0 or cover <= 0:
        is_pet_support_finished = True
        break

if is_pet_support_finished:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000 :.2f}, "
          f"Hay: {hay / 1000 :.2f}, Cover: {cover / 1000 :.2f}.")

