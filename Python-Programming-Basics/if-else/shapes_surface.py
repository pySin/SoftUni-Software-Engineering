# Shapes Surface
from math import pi

shape = input()
area = 0
# square, rectangle, circle или triangle
if shape == "square":
    side_a = float(input())
    area = side_a * side_a
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif shape == "circle":
    r = float(input())
    area = pi * r**2
elif shape == "triangle":
    side_a = float(input())
    side_a_height = float(input())
    area = (side_a * side_a_height) / 2

print(f"{area:.3f}")
