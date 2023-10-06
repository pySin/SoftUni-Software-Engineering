# Radians to Degrees
from math import degrees


def radians_to_degrees(rad):
    return round(degrees(rad), 1)


radians_input = int(input())
get_degrees = radians_to_degrees(radians_input)
print(get_degrees)
