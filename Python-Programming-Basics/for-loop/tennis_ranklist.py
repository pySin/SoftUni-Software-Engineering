# Tennis Ranklist

from math import floor

# ⦁	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# ⦁	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# ⦁	Достигнат етап от турнира – текст – "W", "F" или "SF"

number_of_tournaments = int(input())
initial_number_of_points = int(input())

total_points = initial_number_of_points

WINNING_POINTS = 2000
FINALIST_POINTS = 1200
SEMI_FINALIST_POINTS = 720
tournaments_won = 0

for _ in range(number_of_tournaments):
    tournament_stage = input()

    if tournament_stage == "W":
        tournaments_won += 1
        total_points += WINNING_POINTS
    if tournament_stage == "F":
        total_points += FINALIST_POINTS
    if tournament_stage == "SF":
        total_points += SEMI_FINALIST_POINTS

print(f"Final points: {total_points}")
points_per_tournament = (total_points - initial_number_of_points) / number_of_tournaments
print(f"Average points: {floor(points_per_tournament)}")
won_tournaments = (tournaments_won / number_of_tournaments) * 100
print(f"{won_tournaments :.2f}%")
