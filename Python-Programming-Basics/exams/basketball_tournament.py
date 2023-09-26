# Basketball tournament

# Име на турнира – текст
# За всеки турнир n на брой мача – цяло число в интервала [1…15]
# За всеки мач се четат по два реда:
# Точки, вкарани от отбора на Деси – цяло число в интервала от [0…150]
# Точки, вкарани от противниковия отбор – цяло число в интервала от [0…150]

wins = 0
loss = 0
games_played = 0

while True:
    tournament_name = input()

    if tournament_name == "End of tournaments":
        print(f"{ (wins / games_played) * 100 :.2f}% matches win")
        print(f"{ (loss / games_played) * 100 :.2f}% matches lost")
        break

    games_per_tournament = int(input())

    x = 0
    while games_per_tournament > x:
        x += 1
        games_played += 1
        desi_team_points = int(input())
        contender_points = int(input())

        if desi_team_points > contender_points:
            wins += 1
            print(f"Game {x} of tournament {tournament_name}: win with "
                  f"{desi_team_points - contender_points} points.")
        elif contender_points > desi_team_points:
            loss += 1
            print(f"Game {x} of tournament {tournament_name}"
                  f": lost with {contender_points - desi_team_points} points.")
