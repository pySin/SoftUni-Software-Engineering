# Longer Line
import math


def length():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    closest_point = None

    if (abs(x1)**2) + (abs(y1)**2) <= (abs(x2)**2) + (abs(y2)**2):
        closest_point = ((math.floor(x1), math.floor(y1)), (math.floor(x2), math.floor(y2)))
    elif (abs(x2)**2) + (abs(y2)**2) < (abs(x1)**2) + (abs(y1)**2):
        closest_point = ((math.floor(x2), math.floor(y2)), (math.floor(x1), math.floor(y1)))

    leg_1 = 0

    if x1 >= 0 >= x2 or x1 <= 0 <= x2:
        leg_1 = abs(x1) + abs(x2)
    elif x1 >= 0 and x2 >= 0 or x1 <= 0 and x2 <= 0:
        leg_1 = abs(abs(x1) - abs(x2))

    leg_2 = 0

    if y1 >= 0 >= y2 or y1 <= 0 <= y2:
        leg_2 = abs(y1) + abs(y2)
    elif y1 >= 0 and y2 >= 0 or y1 <= 0 and y2 <= 0:
        leg_2 = abs(abs(y1) - abs(y2))

    return closest_point, math.sqrt((leg_1**2) + (leg_2**2))


def call_functions():
    length_1 = length()
    length_2 = length()

    if length_1[1] > length_2[1]:
        result = ""
        for point in length_1[0]:
            result += str(point)
        return result
    else:
        result = ""
        for point in length_2[0]:
            result += str(point)
        return result


if __name__ == "__main__":
    print(call_functions())
