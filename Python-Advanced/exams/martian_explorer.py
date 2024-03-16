# Martian Explorer


def create_matrix(rows_count: int):

    matrix_c = []
    for _ in range(rows_count):
        make_row = [r for r in input().split()]
        matrix_c.append(make_row)

    return matrix_c


def starting_point(matrix_f: list, starting_s: str) -> list:
    for i in range(len(matrix_f)):
        for j in range(len(matrix_f[0])):
            if matrix[i][j] == starting_s:
                return [i, j]
    return ["Problem finding starting point"]


def matrix_print(matrix_: list):
    for row_ in matrix_:
        print(row_)


def new_position(command_, row_, col_):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1)
    }

    new_row_, new_col_ = row_ + directions[command_][0], col_ + directions[command_][1]
    if new_row_ < 0:
        new_row_ = 5
    elif new_row_ > 5:
        new_row_ = 0

    if new_col_ < 0:
        new_col_ = 5
    elif new_col_ > 5:
        new_col_ = 0
    return new_row_, new_col_


matrix = create_matrix(6)
rover_sign = "E"
row, col = starting_point(matrix, rover_sign)
water_deposit = "W"
metal_deposit = "M"
concrete_deposit = "C"
rock = "R"
normal_sign = "-"

water_collected = 0
metal_collected = 0
concrete_collected = 0


commands = input().split(", ")

for command in commands:
    new_row, new_column = new_position(command, row, col)
    if matrix[new_row][new_column] == water_deposit:
        water_collected += 1
        print(f"Water deposit found at ({new_row}, {new_column})")
    elif matrix[new_row][new_column] == metal_deposit:
        print(f"Metal deposit found at ({new_row}, {new_column})")
        metal_collected += 1
    elif matrix[new_row][new_column] == concrete_deposit:
        print(f"Concrete deposit found at ({new_row}, {new_column})")
        concrete_collected += 1
    elif matrix[new_row][new_column] == "R":
        print(f"Rover got broken at ({new_row}, {new_column})")
        break

    matrix[row][col] = normal_sign
    row, col = new_row, new_column
    matrix[row][col] = rover_sign

if water_collected and metal_collected and concrete_collected:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
