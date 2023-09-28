# Football Tournament

# Името на футболния отбор, за който водим статистика - текст
# Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
#  За всяка изиграна среща се прочита отделен ред:
# Резултатът от изиграната среща в един от горепосочените формати – символ с възможности 'W', 'D' и 'L'

team_name = input()
games_played = int(input())

points = 0
win = 0
draw = 0
loss = 0

x = 0
while x < games_played:
    x += 1
    game_result = input()
    if game_result == "W":
        points += 3
        win += 1
    elif game_result == "D":
        points += 1
        draw += 1
    else:
        loss += 1

if games_played < 1:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {win}")
    print(f"## D: {draw}")
    print(f"## L: {loss}")
    print(f"Win rate: {(win / games_played) * 100 :.2f}%")
