# Return More Than One Value from a function

def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    diagonal = (length ** 2 + width ** 2) ** 0.5
    return area, perimeter, round(diagonal, 2)


area_x, perimeter_x, diagonal_x = calculate_rectangle_properties(12, 7)
