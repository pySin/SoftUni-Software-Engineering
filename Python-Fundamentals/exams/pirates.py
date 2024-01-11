# P!rates


def get_cities():
    cities = {}
    command = input()

    while command != "Sail":
        city_data = command.split("||")
        city_name = city_data[0]
        population = int(city_data[1])
        gold = int(city_data[2])
        if city_name in cities:
            cities[city_name][0] += population
            cities[city_name][1] += gold
        else:
            cities[city_name] = [population, gold]
        command = input()
    return cities


def plunder(cities: dict, command: list):
    town = command[1]
    people = int(command[2])
    gold = int(command[3])
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    cities[town][0] -= people
    cities[town][1] -= gold
    if cities[town][0] <= 0 or cities[town][1] <= 0:
        print(f"{town} has been wiped off the map!")
        cities.pop(town)
    return cities


def prosper(cities: dict, command: list):
    town = command[1]
    gold = int(command[2])
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    return cities


def call_functions():
    cities = get_cities()

    command = input()

    while command != "End":
        command = command.split("=>")
        action = command[0]

        if action == "Plunder":
            cities = plunder(cities, command)
        elif action == "Prosper":
            cities = prosper(cities, command)

        command = input()

    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for city in cities:
            print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


if __name__ == "__main__":
    call_functions()
