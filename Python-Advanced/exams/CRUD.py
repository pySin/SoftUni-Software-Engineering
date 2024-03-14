# CRUD

def create_matrix(rows_count: int):

    matrix_c = []
    for _ in range(rows_count):
        make_row = [r for r in input().strip().split(" ")]
        matrix_c.append(make_row)

    return matrix_c


def matrix_print(matrix_: list):
    for row_ in matrix_:
        print(" ".join(row_))


n = 6
matrix = create_matrix(n)
row, col = [int(rc) for rc in input()[1:-1].split(", ")]
normal_sign = "."

# Create movement Dictionary
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

command = input()

while command != "Stop":
    instructions = command.split(", ")
    action = instructions[0]
    direction = instructions[1]
    new_row, new_col = row + directions[direction][0], col + directions[direction][1]

    if action == "Create":
        value = instructions[2]
        if matrix[new_row][new_col] == normal_sign:
            matrix[new_row][new_col] = value
    elif action == "Update":
        value = instructions[2]
        if matrix[new_row][new_col] != normal_sign:
            matrix[new_row][new_col] = value
    elif action == "Delete":
        if matrix[new_row][new_col] != normal_sign:
            matrix[new_row][new_col] = normal_sign
    elif action == "Read":
        if matrix[new_row][new_col] != normal_sign:
            print(matrix[new_row][new_col])

    # matrix[row][col] = normal_sign
    row, col = new_row, new_col
    # matrix[row][col] = "P"

    command = input()

matrix_print(matrix)
