# Bals
from math import floor

# От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# След това се четат N на брой цветове.

balls_count = int(input())
points = 0

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_balls = 0

for _ in range(balls_count):
    current_ball = input()

    if current_ball == "red":
        points += 5
        red_balls += 1
    elif current_ball == "orange":
        points += 10
        orange_balls += 1
    elif current_ball == "yellow":
        points += 15
        yellow_balls += 1
    elif current_ball == "white":
        points += 20
        white_balls += 1
    elif current_ball == "black":
        points = floor(points / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
