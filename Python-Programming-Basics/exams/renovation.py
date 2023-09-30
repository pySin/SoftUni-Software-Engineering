# Renovation
from math import ceil


wall_height = int(input())
wall_width = int(input())
non_painted_percent = int(input())
# liters_paint = int(input())

paint_surface = ceil(((wall_height * wall_width) * 4) * (1 - (non_painted_percent / 100)))
liters = 0

while True:

    if paint_surface == liters:
        print("All walls are painted! Great job, Pesho!")
        break

    if liters > paint_surface:
        print(f"All walls are painted and you have {liters - paint_surface} l paint left!")
        break

    paint_added = input()

    if paint_added == "Tired!":
        print(f"{paint_surface - liters} quadratic m left.")
        break

    liters += int(paint_added)
