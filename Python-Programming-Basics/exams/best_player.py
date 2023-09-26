# Best Player

# Име на играч – текст
# Брой вкарани голове  – цяло положително число в интервала [1 … 10000]

best_player = ""
top_goals = 0
number_of_games = 0

name_command = input()
while name_command != "END":
    number_of_games += 1
    goals_scored = int(input())

    if goals_scored > top_goals:
        top_goals = goals_scored
        best_player = name_command

    if goals_scored >= 10:
        break

    name_command = input()

print(f"{best_player} is the best player!")
if top_goals >= 3:
    print(f"He has scored {top_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_goals} goals.")
