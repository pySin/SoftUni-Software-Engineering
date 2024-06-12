# Radians to Degrees
from math import pi


def radians_to_degrees(rad):
    return round(rad * (180/pi), 1)


print(radians_to_degrees(20))
