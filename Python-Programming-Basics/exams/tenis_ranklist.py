# Tennis Ranklist
from math import floor


# Брой турнири, в които е участвал – цяло число в интервала [1…20]
# Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# Достигнат етап от турнира – текст – "W", "F" или "SF"

number_of_challenges = int(input())
initial_points = int(input())

points = 0
wins = 0

x = 0
while x < number_of_challenges:
    x += 1
    challenge_stage = input()
    if challenge_stage == "W":
        wins += 1
        points += 2000
    elif challenge_stage == "F":
        points += 1200
    elif challenge_stage == "SF":
        points += 720

final_points = points + initial_points
average_points = points / x
percent_wins = (wins / x) * 100
print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points) :.0f}")
print(f"{percent_wins :.2f}%")
