# football result


# Резултат от първия мач – текст
# Резултат от втория мач – текст
# Резултат от третия мач – текст

first_game_result = input()
second_game_result = input()
third_game_result = input()

win = 0  # "2:0", "0:1", "1:1"
draw = 0
loss = 0

for game_result in (first_game_result, second_game_result, third_game_result):
    # print(game_result)
    first_team = int(game_result[0])
    second_team = int(game_result[2])

    if first_team > second_team:
        win += 1
    elif first_team == second_team:
        draw += 1
    elif second_team > first_team:
        loss += 1


print(f"Team won {win} games.")
print(f"Team lost {loss} games.")
print(f"Drawn games: {draw}")
