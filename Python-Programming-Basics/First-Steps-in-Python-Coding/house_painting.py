# House Painting

DOOR_WIDTH = 1.2
DOOR_HEIGHT = 2

WINDOW_SIDE = 1.5

x = float(input())
y = float(input())
h = float(input())

door_surface = DOOR_WIDTH * DOOR_HEIGHT

front_and_back_walls_surface = ((x * x) * 2) - door_surface

side_walls_surface = ((x * y) * 2) - ((WINDOW_SIDE * WINDOW_SIDE) * 2)
walls_surface = front_and_back_walls_surface + side_walls_surface

green_paint = walls_surface / 3.4
print(f"{green_paint:.2f}")

roof_side_slopes = (x * y) * 2

# The 2 triangles for a square so no need to divide.
roof_front_slopes = (x * h)

roof_whole_surface = roof_front_slopes + roof_side_slopes
red_paint = roof_whole_surface / 4.3
print(f"{red_paint:.2f}")
