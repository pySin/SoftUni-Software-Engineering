# Matrix Template


def get_matrix(n: int) -> list:
    matrix = [list(input()) for _ in range(n)]
    # matrix = [input().split("") for _ in range(n)]
    return matrix


def get_current_position(matrix: list, char: str) -> tuple:
    position = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == char:
                position = i, j
    return position


def up(current_row: int, current_col: int):
    new_row = current_row - 1
    new_col = current_col
    return new_row, new_col


def down(current_row: int, current_col: int):
    new_row = current_row + 1
    new_col = current_col
    return new_row, new_col


def right(current_row: int, current_col: int):
    new_row = current_row
    new_col = current_col + 1
    return new_row, new_col


def left(current_row: int, current_col: int):
    new_row = current_row
    new_col = current_col - 1
    return new_row, new_col


def boundary_check(matrix: list, new_row: int, new_col: int):
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
        return True
    else:
        return False


def change_position(matrix: list, row: int, col: int, new_row: int, new_col: int, normal_sign: str, player_sign: str):
    matrix[row][col] = normal_sign
    row, col = new_row, new_col
    matrix[row][col] = player_sign
    return matrix, row, col


def call_functions():
    n = int(input())
    player_sign = "S"
    normal_sign = "-"
    matrix = get_matrix(n)
    print(matrix)
    row, col = get_current_position(matrix, player_sign)
    print(f"Row: {row}, Col: {col}")

    command = input()
    while command != "end":
        direction = command.split()[0]
        if direction == "up":
            new_row, new_col = up(row, col)
            matrix, row, col = change_position(matrix, row, col, new_row, new_col, normal_sign, player_sign)
            for c_row in matrix:
                print(c_row)
        if direction == "down":
            new_row, new_col = down(row, col)
            matrix, row, col = change_position(matrix, row, col, new_row, new_col, normal_sign, player_sign)
            for c_row in matrix:
                print(c_row)
        if direction == "left":
            new_row, new_col = left(row, col)
            matrix, row, col = change_position(matrix, row, col, new_row, new_col, normal_sign, player_sign)
            for c_row in matrix:
                print(c_row)
        if direction == "right":
            new_row, new_col = right(row, col)
            matrix, row, col = change_position(matrix, row, col, new_row, new_col, normal_sign, player_sign)
            for c_row in matrix:
                print(c_row)
        command = input()


if __name__ == "__main__":
    call_functions()
