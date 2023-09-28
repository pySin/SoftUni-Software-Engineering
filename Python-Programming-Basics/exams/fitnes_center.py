# Fitness Center

# На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
# За всеки един посетител на отделен ред – дейността във фитнеса – текст
# ("Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar")

number_of_visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

training = 0
shopping = 0

x = 0
while x < number_of_visitors:
    x += 1
    activity = input()

    if activity == "Back":
        back += 1
        training += 1
    elif activity == "Chest":
        chest += 1
        training += 1
    elif activity == "Legs":
        legs += 1
        training += 1
    elif activity == "Abs":
        abs += 1
        training += 1
    elif activity == "Protein shake":
        protein_shake += 1
        shopping += 1
    elif activity == "Protein bar":
        protein_bar += 1
        shopping += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(training / x) * 100 :.2f}% - work out")
print(f"{(shopping / x) * 100 :.2f}% - protein")
