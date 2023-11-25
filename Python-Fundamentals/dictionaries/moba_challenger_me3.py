# Moba Challenger


def manage_user(command, players_data):
    name = command[0]
    position = command[1]
    skill = int(command[2])

    if name not in players_data:
        players_data[name] = {position: skill}
    else:
        if position not in players_data[name]:
            players_data[name][position] = skill
        else:
            if skill > players_data[name][position]:
                players_data[name][position] = skill
    return players_data


def manage_battles(command, players_data):
    player_1, vs, player_2 = command[0].split()
    if player_1 in players_data and player_2 in players_data:
        for position in players_data[player_1]:
            if position in players_data[player_2]:
                player_1_total = sum(players_data[player_1].values())
                player_2_total = sum(players_data[player_2].values())
                if player_1_total > player_2_total:
                    del players_data[player_2]
                elif player_1_total < player_2_total:
                    del players_data[player_1]
    return players_data


def display_data(players_data):
    # print(players_data)
    names_order = sorted(players_data)
    names_order = sorted([[name, sum(players_data[name].values())]
                          for name in names_order], key=lambda x: x[1], reverse=True)
    # print(names_order)
    for name, total_points in names_order:
        print(f"{name}: {total_points} skill")
        ordered_position = sorted(players_data[name])
        ordered_position = sorted([[position, players_data[name][position]] for position in ordered_position],
                                  key=lambda x: x[1], reverse=True)
        for position, amount in ordered_position:
            print(f"- {position} <::> {amount}")
        # print(ordered_position)

    # names_order = sorted(players_data.items())
    # skil_name_order = sorted(names_order, key=lambda x: sum(x[1].values()), reverse=True)
    # # print(skil_name_order)
    # for name, value in skil_name_order:
    #     print(f"{name}: {sum(value.values())} skill")
    #     value = sorted(value.items(), key=lambda x: x[0])
    #     value = sorted(value, key=lambda x: x[1], reverse=True)
    #     for position in value:
    #         print(f"- {position[0]} <::> {position[1]}")


def function_call():
    command = input().split(" -> ")
    players_data = {}

    while command != ["Season end"]:
        if " vs " not in command[0]:
            players_data = manage_user(command, players_data)
        else:
            players_data = manage_battles(command, players_data)

        command = input().split(" -> ")

    # print(players_data)
    display_data(players_data)


if __name__ == "__main__":
    function_call()
