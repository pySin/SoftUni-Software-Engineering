# Gues the full name with functions

CORRECT_FAMILY_NAME = "Mehmedov"
CORRECT_SECOND_NAME = "Kqazimov"
CORRECT_FIRST_NAME = "Sinan"

person_names = [CORRECT_FAMILY_NAME, CORRECT_SECOND_NAME, CORRECT_FIRST_NAME]


def get_input():
    name = input()
    return name


def check_name(name, guesses_count):
    if name == person_names[guesses_count]:
        if guesses_count > 2:
            return False
        print(f"Correct name: {person_names[guesses_count]}")
        return False
    else:
        #  print(f"The name you entered is not {person_names[guesses_count]}")
        return True


new_name = ""
guesses = 0
while check_name(new_name, guesses):
    while check_name(new_name, guesses):
        while check_name(new_name, guesses):
            print(guesses)
            print("Inner Loop")
            new_name = get_input()

        # if guesses < len(person_names) - 1:
        guesses += 1
