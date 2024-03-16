# Matrix template

def create_matrix(rows_count: int):

    matrix_c = []
    for _ in range(rows_count):
        # make_row = [r for r in list(input())]
        make_row = [r for r in input().split()]
        matrix_c.append(make_row)

    for r in matrix_c:
        print(r)
    return matrix_c


def starting_point(matrix_f: list, starting_s: str) -> list:
    for i in range(len(matrix_f)):
        for j in range(len(matrix_f[0])):
            if matrix[i][j] == starting_s:
                print(f"Starting row: {i}, Starting column: {j}")
                return [i, j]
    print("Problem finding starting point")
    return ["Problem finding starting point"]


def boundary_check(matrix_c: list, new_row_c: int, new_col_c: int):
    if 0 <= new_row_c < len(matrix_c) and 0 <= new_col_c < len(matrix_c[0]):
        return True
    else:
        return False


def matrix_print(matrix_: list):
    for row_ in matrix_:
        print("".join(row_))


def next_position(curr_row, curr_col, direction):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1)
    }

    new_row_ = curr_row + directions[direction][0]
    new_col_ = curr_col + directions[direction][1]

    # if new_col_ == len(matrix[0]):
    #     new_col_ = 0
    # elif new_col_ == -1:
    #     new_col_ = len(matrix[0]) - 1
    #
    # if new_row_ == len(matrix):
    #     new_row_ = 0
    # elif new_row_ == -1:
    #     new_row_ = len(matrix) - 1

    return new_row_, new_col_

# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "right": (0, 1),
#     "left": (0, -1)
# }


rows, cols = [int(r) for r in input().split(", ")]
p_sign = "w"
normal_sign = "-"
matrix = create_matrix(rows)
row, col = starting_point(matrix, p_sign)

command = input()
while command != "danger":

    # new_row, new_col = row + directions[command][0], col + directions[command][1]
    new_row, new_col = next_position(row, col, command)

    # if not boundary_check(matrix, new_row, new_col):
    #     print("You are out of the matrix!")
    #     break
    # if matrix[new_row][new_col} == ?
    matrix[new_row][new_col], matrix[row][col] = p_sign, normal_sign
    matrix_print(matrix)

    row, col = new_row, new_col
    command = input()

# def get_matrix(n: int) -> list:
#     matrix = [list(input()) for _ in range(n)]
#     # matrix = [input().split("") for _ in range(n)]
#     return matrix
#
#
# def get_current_position(matrix: list, char: str) -> tuple:
#     position = None
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] == char:
#                 position = i, j
#     return position
#
#
# def up(current_row: int, current_col: int):
#     new_row = current_row - 1
#     new_col = current_col
#     return new_row, new_col
#
#
# def down(current_row: int, current_col: int):
#     new_row = current_row + 1
#     new_col = current_col
#     return new_row, new_col
#
#
# def right(current_row: int, current_col: int):
#     new_row = current_row
#     new_col = current_col + 1
#     return new_row, new_col
#
#
# def left(current_row: int, current_col: int):
#     new_row = current_row
#     new_col = current_col - 1
#     return new_row, new_col
#
#
# def boundary_check(matrix: list, new_row: int, new_col: int):
#     if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#         return True
#     else:
#         return False
#
#
# def call_functions():
#     n = int(input())
#     matrix = get_matrix(n)
#     print(matrix)
#     row, col = get_current_position(matrix, "S")
#     print(f"Row: {row}, Col: {col}")
#
#
# if __name__ == "__main__":
#     call_functions()
