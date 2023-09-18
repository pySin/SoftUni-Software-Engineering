# For plus While plus Dictionary
# Land subsidies

SUBSIDY_OVER_5_to_100 = 8456
SUBSIDY_LESS_5 = 9800

while True:
    today_date = input("Enter date in dd.month_name.yyyy format or \"Over\" to finish:")
    if today_date == "Over":
        break

    if today_date[0:2].isnumeric() and today_date[3:-5:1].isalpha() and today_date[-4:].isnumeric():
        print("Date format is correct :)")
    else:
        print("Insert a valid date format:")
        continue

    land_owners = ["Ivan", "Petar", "Sinan", "Hristo", "Vasko"]
    owners_dict = {}
    for owner in land_owners:
        while True:
            try:
                current_land_size = int(input(f"Insert {owner}\'s size of land in hectares!"))
                if 1 <= current_land_size <= 5:
                    print("Your subsidy for 2024 is: " + str(current_land_size * SUBSIDY_LESS_5))
                    owners_dict[owner] = current_land_size * SUBSIDY_LESS_5
                    break
                elif 5 < current_land_size < 100:
                    print("Your subsidy for 2024 is: " + str(current_land_size * SUBSIDY_OVER_5_to_100))
                    owners_dict[owner] = current_land_size * SUBSIDY_OVER_5_to_100
                    break
                elif current_land_size < 1:
                    print("You must have at least 1 hectare!")
                else:
                    print("No subsidies for over 100 Hectares!")
            except ValueError:
                print("You must insert a whole number!")

    print(owners_dict)
