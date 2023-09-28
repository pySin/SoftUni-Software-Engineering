# Darts

# Името на играча - текст
# След това до получаване на команда "Retire" се четат многократно по два реда:
# Поле – текст ("Single", "Double" или "Triple")
# Точки – цяло число в интервала [0… 100]

player_name = input()
points_left = 301

x = 0
y = 0
while True:
    hit_multi = input()  # "Single", "Double" или "Triple"
    if hit_multi == "Retire":
        print(f"{player_name} retired after {y} unsuccessful shots.")
        break

    points = int(input())
    x += 1

    current_points = 0

    if hit_multi == "Single":
        current_points += points
    elif hit_multi == "Double":
        current_points += points * 2
    elif hit_multi == "Triple":
        current_points += points * 3

    if current_points > points_left:
        y += 1
    elif current_points < points_left:
        points_left -= current_points
    elif current_points == points_left:
        print(f"{player_name} won the leg with {x - y} shots.")
        break
