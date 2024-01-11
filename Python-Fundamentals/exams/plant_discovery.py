# Plant discovery


def add_plant(plants: dict) -> dict:
    new_plant = input().split("<->")
    plant_name = new_plant[0]
    plant_rarity = new_plant[1]
    plants[plant_name] = [plant_rarity]
    return plants


def rate_plants(plants: dict, instruction: list) -> dict:
    plant, rating = instruction[1].split(" - ")
    if plant not in plants:
        print("error")
    else:
        plants[plant].append(int(rating))
    return plants


def update_plant(plants: dict, instruction: list) -> dict:
    plant, new_rarity = instruction[1].split(" - ")
    if plant in plants:
        plants[plant][0] = new_rarity
    else:
        print("error")
    return plants


def reset_plant(plants: dict, instruction: list) -> dict:
    plant = instruction[1]
    if plant in plants:
        plants[plant] = [plants[plant][0]]
    else:
        print("error")
    return plants


def display_plants(plants: dict):
    print("Plants for the exhibition:")
    for plant in plants:
        rarity = plants[plant][0]
        rating = 0 if len(plants[plant]) < 2 else (sum(plants[plant][1:]) / len(plants[plant][1:]))
        print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")


def call_functions():
    plants = {}
    number_of_plants = int(input())
    for _ in range(number_of_plants):
        plants = add_plant(plants)

    command = input()

    while command != "Exhibition":

        instruction = command.split(": ")

        if instruction[0] == "Rate":
            plants = rate_plants(plants, instruction)
        elif instruction[0] == "Update":
            plants = update_plant(plants, instruction)
        elif instruction[0] == "Reset":
            plants = reset_plant(plants, instruction)
        command = input()

    # Display Plants
    display_plants(plants)


if __name__ == "__main__":
    call_functions()
