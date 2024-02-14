# Matrix Modification


def create_matrix(rows: int) -> list:
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    return matrix


def modify_number(matrix: list, instructions: list, rows: int) -> list:
    action = instructions[0]
    row = int(instructions[1])
    col = int(instructions[2])
    value = int(instructions[3])

    actions = {
        "Add": lambda x, y: x + y,
        "Subtract": lambda x, y: x - y
    }

    if 0 <= row < rows and 0 <= col < rows:
        # if row < 0 or row >= rows or col < 0 or col >= rows
        matrix[row][col] = actions[action](matrix[row][col], value)
        # if action == "Add":
        #     matrix[row][col] += value
        # elif action == "Subtract":
        #     matrix[row][col] -= value

    else:
        print(f"Invalid coordinates")

    return matrix


def call_functions():
    rows = int(input())
    matrix = create_matrix(rows)

    command = input()

    while command != "END":
        instructions = command.split()
        matrix = modify_number(matrix, instructions, rows)
        command = input()
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    call_functions()
