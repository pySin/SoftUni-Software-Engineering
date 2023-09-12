# Fuel Tank 1

type_of_fuel = input()
fuel_in_tank = float(input())

type_of_fuel_check = ""

if type_of_fuel == "Diesel":
    type_of_fuel_check = "diesel"
elif type_of_fuel == "Gasoline":
    type_of_fuel_check = "gasoline"
elif type_of_fuel == "Gas":
    type_of_fuel_check = "gas"
else:
    pass

if type_of_fuel_check == "":
    print("Invalid fuel!")
elif fuel_in_tank >= 25:
    print(f"You have enough {type_of_fuel_check}.")
else:
    print(f"Fill your tank with {type_of_fuel_check}!")
