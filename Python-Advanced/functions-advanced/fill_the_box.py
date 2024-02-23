# Fill The Box


def fill_the_box(height, length, width, *args):
    space_available = height * length * width
    space_filled = 0
    for cube in args:
        if cube == "Finish":
            return f"There is free space in the box. You could put {space_available - space_filled} more cubes."
        if space_filled + cube > space_available:
            remaining_cubes = sum(args[:-1]) - space_available
            return f"No more free space! You have {remaining_cubes} more cubes."
        space_filled += cube
    return f"There is free space in the box. You could put {space_available - space_filled} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
