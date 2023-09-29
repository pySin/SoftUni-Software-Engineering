# Movie Star

# Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
# След това се четат многократно по един или два реда до команда "ACTION" или до изчерпване на бюджета:
# Име на актьор - текст
# Ако името на актьора съдържа по-малко или равно на 15 брой символи:
# Възнаграждение - реално число в интервала [250.0… 1 000 000.0]


budget = float(input())

while True:
    actor_name = input()

    if actor_name == "ACTION":
        print(f"We are left with {budget :.2f} leva.")
        break

    if len(actor_name) > 15:
        pay = budget * 0.20
    else:
        pay = float(input())

    budget -= pay
    if budget < 0:
        print(f"We need {abs(budget) :.2f} leva for our actors.")
        break
