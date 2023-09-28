# Easter Eggs Battle

# Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда "End" се четe многократно един ред:
# Победител - текст - "one" или "two"

first_player_eggs = int(input())
second_player_eggs = int(input())

winner = ""

while True:

    winner = input()

    if winner == "End":
        print(f"Player one has {first_player_eggs} eggs left.")
        print(f"Player two has {second_player_eggs} eggs left.")
        break

    if winner == "one":
        second_player_eggs -= 1
    elif winner == "two":
        first_player_eggs -= 1

    if first_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
        break
    elif second_player_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
        break
