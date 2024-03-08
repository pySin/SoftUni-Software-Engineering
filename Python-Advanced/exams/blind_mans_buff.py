# Blind Man's Buff

def create_matrix(rows_count: int):

    matrix_c = []
    for _ in range(rows_count):
        # make_row = [r for r in list(input())]
        make_row = [r for r in input().split()]
        matrix_c.append(make_row)
    return matrix_c


def starting_point(matrix_f: list, starting_s: str) -> list:
    for i in range(len(matrix_f)):
        for j in range(len(matrix_f[0])):
            if matrix[i][j] == starting_s:
                return [i, j]
    return ["Problem finding starting point"]


def boundary_check(matrix_c: list, new_row_c: int, new_col_c: int):
    if 0 <= new_row_c < len(matrix_c) and 0 <= new_col_c < len(matrix_c[0]):
        return True
    else:
        return False


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}


n, m = [int(x) for x in input().split()]
p_sign = "B"
normal_sign = "-"
matrix = create_matrix(n)
row, col = starting_point(matrix, p_sign)
matrix[row][col] = normal_sign  # NC
moves_made = 0
opponents_touched = 0

command = input()
while command != "Finish":
    new_row, new_col = row + directions[command][0], col + directions[command][1]
    if not boundary_check(matrix, new_row, new_col) or matrix[new_row][new_col] == "O":
        command = input()
        continue
    elif matrix[new_row][new_col] == normal_sign:
        moves_made += 1
    elif matrix[new_row][new_col] == "P":
        moves_made += 1
        opponents_touched += 1
        if opponents_touched == 3:
            matrix[new_row][new_col] = normal_sign
            break
    matrix[row][col] = normal_sign
    row, col = new_row, new_col
    matrix[row][col] = p_sign

    command = input()


print("Game over!")
print(f"Touched opponents: {opponents_touched} Moves made: {moves_made}")
