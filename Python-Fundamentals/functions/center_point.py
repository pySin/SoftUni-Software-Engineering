# Center Point cartesian
from math import floor


def abs_sum(x, y):
    return (floor(x), floor(y)), abs(x) + abs(y)


def function_call():
    position_1 = abs_sum(float(input()), float(input()))
    position_2 = abs_sum(float(input()), float(input()))

    if position_1[1] <= position_2[1]:
        return position_1[0]
    else:
        return position_2[0]


if __name__ == "__main__":
    print(function_call())
