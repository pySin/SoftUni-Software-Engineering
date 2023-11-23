# Dragon Army


def get_dragons_data():
    n = int(input())

    dragon_data = {}

    for _ in range(n):
        command = input().split()
        dragon_type = command[0]
        name = command[1]
        damage = int(command[2]) if command[2] != "null" else 45
        health = int(command[3]) if command[3] != "null" else 250
        armor = int(command[4]) if command[4] != "null" else 10

        if dragon_type not in dragon_data:
            dragon_data[dragon_type] = {name: [damage, health, armor]}
        else:
            dragon_data[dragon_type][name] = [damage, health, armor]
    return dragon_data


def order_dragons_data(dragon_data):
    for dragon_type in dragon_data:
        dragon_data[dragon_type] = sorted(dragon_data[dragon_type].items())
    return dragon_data


def display_dragons_data(dragons_data):  # Red::(160.00/2350.00/30.00)
    for dragon_type in dragons_data:
        average_damage = sum([ad[1][0] for ad in dragons_data[dragon_type]]) / len(dragons_data[dragon_type])
        average_health = sum([ad[1][1] for ad in dragons_data[dragon_type]]) / len(dragons_data[dragon_type])
        average_armor = sum([ad[1][2] for ad in dragons_data[dragon_type]]) / len(dragons_data[dragon_type])
        print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
        for single_dragon in dragons_data[dragon_type]:
            print(f"-{single_dragon[0]} -> damage: {single_dragon[1][0]}, "
                  f"health: {single_dragon[1][1]}, armor: {single_dragon[1][2]}")
        # print(average_damage)
        # print(average_health)
        # print(average_armor)


def function_call():
    dragon_data = get_dragons_data()
    # print(dragon_data)
    dragon_data = order_dragons_data(dragon_data)
    # print(dragon_data)
    display_dragons_data(dragon_data)


if __name__ == "__main__":
    function_call()
