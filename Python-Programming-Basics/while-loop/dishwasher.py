# Dishwasher

# Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
# На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се
# изчерпи, брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]

detergent_bottles = int(input())

whole_detergents_in_ml = detergent_bottles * 750
number_of_washes = 0
dishes_washed_count = 0
pots_washed_count = 0

command = input()
while command != "End":
    number_of_washes += 1
    current_dishes = int(command)

    if number_of_washes % 3 == 0:
        whole_detergents_in_ml -= current_dishes * 15
        pots_washed_count += current_dishes
    else:
        whole_detergents_in_ml -= current_dishes * 5
        dishes_washed_count += current_dishes

    if whole_detergents_in_ml < 0:
        break

    command = input()

if whole_detergents_in_ml >= 0:
    print(f"Detergent was enough!")
    print(f"{dishes_washed_count} dishes and {pots_washed_count} pots were washed.")
    print(f"Leftover detergent {whole_detergents_in_ml} ml.")
else:
    print(f"Not enough detergent, {abs(whole_detergents_in_ml)} ml. more necessary!")
