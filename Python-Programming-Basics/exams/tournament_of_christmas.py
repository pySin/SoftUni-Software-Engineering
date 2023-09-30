# Tournament Of Christmas

# Първоначално от конзолата се прочита броя дни на турнира – цяло число в интервала [1… 20]
# До получаване на командата "Finish" се чете:
# Спорт  – текст
# За всеки спорт се прочита:
# Резултат  – текст с възможности: "win" или "lose"

tournament_days = int(input())
money_collected = 0

win_days_count = 0
loose_days_count = 0

for _ in range(tournament_days):

    days_money = 0
    days_win = 0
    days_loose = 0

    while True:
        sport = input()

        if sport == "Finish":
            break

        result = input()  # "win", "loose"

        if result == "win":
            days_money += 20
            days_win += 1
        elif result == "lose":
            days_loose += 1

    if days_win > days_loose:
        days_money *= 1.10
        win_days_count += 1
    else:
        loose_days_count += 1

    money_collected += days_money


if win_days_count > loose_days_count:
    money_collected *= 1.20
    print(f"You won the tournament! Total raised money: {money_collected :.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_collected :.2f}")
