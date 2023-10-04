# Five Players Names
name = input("Insert a player\'s first name and family name: ")

player_number = 1
is_no_enough_players = False
for _ in range(5):
    while player_number < 5 and " " in name:
        # print("In While Loop")
        if "Stop" in name:
            is_no_enough_players = True
            break
        print(f"{name} is the {player_number} player!")
        if is_no_enough_players:
            break
        name = input("Insert a player\'s first name and family name: ")
        player_number += 1

if is_no_enough_players:
    print(f"There are no enough players!")
else:
    print(f"Enough players for the game!")
