# Sorting hat

name = input()

is_valdemort = False
while name != "Welcome!":

    if name == "Voldemort":
        print(f"You must not speak of that name!")
        is_valdemort = True
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if not is_valdemort:
    print("Welcome to Hogwarts.")
