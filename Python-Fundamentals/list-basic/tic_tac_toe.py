# Tic Tac Toe

FIRST_PLAYER_WIN = 3
SECOND_PLAYER_WIN = 6

line_one = [int(item) for item in input().split()]
line_two = [int(item) for item in input().split()]
line_three = [int(item) for item in input().split()]


if 2 not in line_one and 0 not in line_one or 2 not in line_two and 0 not in line_two or \
        2 not in line_three and 0 not in line_three:
    print("First player won")
elif 1 not in line_one and 0 not in line_one or 1 not in line_two and 0 not in line_two or \
        1 not in line_three and 0 not in line_three:
    print("Second player won")
elif line_one[0] == 1 and line_two[0] == 1 and line_three[0] == 1 \
        or line_one[1] == 1 and line_two[1] == 1 and line_three[1] == 1 \
        or line_one[2] == 1 and line_two[2] == 1 and line_three[2] == 1:
    print("First player won")
elif line_one[0] == 2 and line_two[0] == 2 and line_three[0] == 2 \
        or line_one[1] == 2 and line_two[1] == 2 and line_three[1] == 2 \
        or line_one[2] == 2 and line_two[2] == 2 and line_three[2] == 2:
    print("Second player won")
elif line_one[0] == 1 and line_two[1] == 1 and line_three[2] == 1 \
        or line_one[2] == 1 and line_two[1] == 1 and line_three[0] == 1:
    print("First player won")
elif line_one[0] == 2 and line_two[1] == 2 and line_three[2] == 2 \
        or line_one[2] == 2 and line_two[1] == 2 and line_three[0] == 2:
    print("Second player won")
else:
    print("Draw!")
