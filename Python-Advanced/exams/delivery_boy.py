# Delivery Boy

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


def change_position(matrix: list, row: int, col: int, new_row: int, new_col: int, normal_sign: str,
                    initial_row: int, initial_col: int):
    if not boundary_check(matrix, new_row, new_col):
        if matrix[row][col] == "P":
            matrix[row][col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        else:
            matrix[row][col] = normal_sign
        matrix[initial_row][initial_col] = " "
        print("The delivery is late. Order is canceled.")
        return matrix, row, col, True
    elif matrix[new_row][new_col] == "A":
        matrix[new_row][new_col] = "P"
        matrix[row][col] = normal_sign
        matrix[initial_row][initial_col] = "B"
        print("Pizza is delivered on time! Next order...")
        return matrix, row, col, True
    elif matrix[new_row][new_col] == "*":
        return matrix, row, col, False
    if matrix[row][col] == "P":
        matrix[row][col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
    else:
        matrix[row][col] = normal_sign
    row, col = new_row, new_col
    return matrix, row, col, False


def call_functions():
    n = int(input().split()[0])
    player_sign = "B"
    normal_sign = "."
    is_game_over = False
    matrix = get_matrix(n)
    # print(matrix)
    row, col = get_current_position(matrix, player_sign)
    initial_row = row
    initial_col = col
    # print(f"Row: {row}, Col: {col}")

    command = input()
    while command != "end":
        direction = command.split()[0]
        if direction == "up":
            new_row, new_col = up(row, col)
            matrix, row, col, is_game_over = change_position(matrix, row, col, new_row, new_col, normal_sign,
                                                             initial_row, initial_col)
            # print("-------")
            # matrix[initial_row][initial_col] = player_sign
            # for c_row in matrix:
            #     print(c_row)
        if direction == "down":
            new_row, new_col = down(row, col)
            matrix, row, col, is_game_over = change_position(matrix, row, col, new_row, new_col, normal_sign,
                                                             initial_row, initial_col)
            # print("-------")
            # for c_row in matrix:
            #     print(c_row)
        if direction == "left":
            new_row, new_col = left(row, col)
            matrix, row, col, is_game_over = change_position(matrix, row, col, new_row, new_col, normal_sign,
                                                             initial_row, initial_col)
            # print("-------")
            # for c_row in matrix:
            #     print(c_row)
        if direction == "right":
            new_row, new_col = right(row, col)
            matrix, row, col, is_game_over = change_position(matrix, row, col, new_row, new_col, normal_sign,
                                                             initial_row, initial_col)
            # print("-------")
            # for c_row in matrix:
            #     print(c_row)

        if is_game_over:
            break
        command = input()

    for f_row in matrix:
        print("".join(f_row))


if __name__ == "__main__":
    call_functions()
