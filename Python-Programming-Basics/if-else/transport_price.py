# Transport Price

number_of_kilometers = int(input())
day_or_night = input()

x = 0
y = 0
if number_of_kilometers < 20:
    x += 5

if day_or_night == "day":
    x += 1

if day_or_night == "night":
    x += 2

if x == 6:
    transport_expenses = 0.70 + (number_of_kilometers * 0.79)
    print(f"{transport_expenses :.2f}")
elif x == 7:
    transport_expenses = 0.70 + (number_of_kilometers * 0.90)
    print(f"{transport_expenses :.2f}")

if number_of_kilometers >= 100:
    transport_expenses = number_of_kilometers * 0.06
    y += 2
    print(f"{transport_expenses :.2f}")

if number_of_kilometers >= 20:
    y += 1

if y == 1:
    transport_expenses = number_of_kilometers * 0.09
    print(f"{transport_expenses :.2f}")
