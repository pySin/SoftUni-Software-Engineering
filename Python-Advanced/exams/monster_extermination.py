# # Monster Extermination
# from collections import deque
#
#
# def single_strike(monsters, strikes, current_armor, current_strike):
#
#     if current_strike > current_armor:
#         if strikes:
#             strikes[-1] += current_strike - current_armor
#         else:
#             strikes = [current_strike - current_armor]
#     elif current_armor > current_strike:
#         monsters.append(current_armor - current_strike)
#     return monsters, strikes


# def call_functions():
#     monsters = deque([int(monster) for monster in input().split(",")])
#     strikes = [int(strike) for strike in input().split(",")]
#     initial_monsters_count = len(monsters)
#     while monsters and strikes:
#         current_armor = monsters.popleft()
#         current_strike = strikes.pop()
#         monsters, strikes = single_strike(monsters, strikes, current_armor, current_strike)
#
#     if not monsters:
#         print("All monsters have been killed!")
#     elif not strikes:
#         print("The soldier has been defeated.")
#
#     print(f"Total monsters killed: {initial_monsters_count - len(monsters)}")
#
#
# if __name__ == "__main__":
#     call_functions()

# -- 2nd try
from collections import deque

monsters = deque([int(m) for m in input().split(",")])
strikes = [int(s) for s in input().split(",")]


killed_monsters = 0
while monsters and strikes:
    current_armor = monsters.popleft()
    current_strike = strikes.pop()
    if current_strike > current_armor:
        if strikes:
            strikes[-1] += current_strike - current_armor
        else:
            strikes = [current_strike - current_armor]
        killed_monsters += 1
    elif current_armor > current_strike:
        monsters.append(current_armor - current_strike)
    else:
        killed_monsters += 1

if not monsters:
    print("All monsters have been killed!")
if not strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
