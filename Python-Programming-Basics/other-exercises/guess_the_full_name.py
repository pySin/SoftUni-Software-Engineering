# Guess The Full Name
# While Trap
CORRECT_FAMILY_NAME = "Mehmedov"
CORRECT_SECOND_NAME = "Kqazimov"
CORRECT_FIRST_NAME = "Sinan"

first_name = ""
second_name = ""
family_name = ""


while first_name != CORRECT_FIRST_NAME:
    while second_name != CORRECT_SECOND_NAME:
        while family_name != CORRECT_FAMILY_NAME:
            family_name = input("Enter your Family Name: ")
            if family_name != CORRECT_FAMILY_NAME:
                print("The Family name is not Mehmedov")
        second_name = input("Enter your Father\'s Name: ")
        if second_name != CORRECT_SECOND_NAME:
            print("The second name is not Kqzimov")
    first_name = input("Enter your first name: ")
    if first_name != CORRECT_FIRST_NAME:
        print("The first name is not Sinan.")
