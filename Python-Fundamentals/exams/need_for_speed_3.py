# Need For Speed 3


def add_cars(number_of_cars: int, cars_options: dict) -> dict:
    for _ in range(number_of_cars):
        car = input().split("|")
        name = car[0]
        mileage = int(car[1])
        fuel = int(car[2])
        cars_options[name] = [mileage, fuel]
    return cars_options


def drive(cars_options: dict, instructions: list) -> dict:
    car = instructions[1]
    distance = int(instructions[2])
    fuel = int(instructions[3])
    if cars_options[car][1] >= fuel:
        cars_options[car][1] -= fuel
        cars_options[car][0] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if cars_options[car][0] > 100000:
        print(f"Time to sell the {car}!")
        cars_options.pop(car)
    return cars_options


def refuel(cars_options: dict, instructions: list) -> dict:
    car = instructions[1]
    fuel = int(instructions[2])
    if cars_options[car][1] + fuel > 75:
        fuel_loaded = 75 - cars_options[car][1]
        cars_options[car][1] = 75
        print(f"{car} refueled with {fuel_loaded} liters")
    else:
        cars_options[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    return cars_options


def revert(car_options: dict, instructions: list) -> dict:
    car = instructions[1]
    kilometers = int(instructions[2])
    if car_options[car][0] - kilometers < 10000:
        car_options[car][0] = 10000
    else:
        car_options[car][0] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return car_options


def call_functions():
    number_of_cars = int(input())

    cars_options = {
        "Drive": drive,
        "Refuel": refuel,
        "Revert": revert
    }

    cars_options = add_cars(number_of_cars, cars_options)

    command = input()

    while command != "Stop":
        instructions = command.split(" : ")
        action = instructions[0]
        cars_options = cars_options[action](cars_options, instructions)
        command = input()

    for car in cars_options:
        if car not in ["Drive", "Refuel", "Revert"]:
            mileage = cars_options[car][0]
            fuel = cars_options[car][1]
            print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


if __name__ == "__main__":
    call_functions()
