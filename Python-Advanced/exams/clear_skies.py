# Clear Skies


def create_matrix(rows_count: int):

    matrix_c = []
    for _ in range(rows_count):
        make_row = [r for r in list(input())]
        matrix_c.append(make_row)

    return matrix_c


def starting_point(matrix_f: list, starting_s: str) -> list:
    for i in range(len(matrix_f)):
        for j in range(len(matrix_f)):
            if matrix[i][j] == starting_s:
                return [i, j]


def next_position(curr_row, curr_col, direction):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1)
    }

    new_row_ = curr_row + directions[direction][0]
    new_col_ = curr_col + directions[direction][1]

    return new_row_, new_col_


def matrix_print(matrix_: list):
    for row_ in matrix_:
        print("".join(row_))


n = int(input())
matrix = create_matrix(n)
jet_fighter = "J"
enemy = "E"
repair = "R"
normal_sign = "-"
ARMOR = 300
ARMOR_LOST_PER_BATTLE = 100
ENEMIES = 4

row, col = starting_point(matrix, jet_fighter)

command = input()
while True:

    new_row, new_col = next_position(row, col, command)
    if matrix[new_row][new_col] == enemy:
        ENEMIES -= 1

        if ENEMIES == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            matrix[new_row][new_col] = jet_fighter
            matrix[row][col] = normal_sign
            break
        else:
            ARMOR -= 100
            if ARMOR == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
                matrix[new_row][new_col] = jet_fighter
                matrix[row][col] = normal_sign
                break
    elif matrix[new_row][new_col] == repair:
        ARMOR = 300

    matrix[new_row][new_col] = jet_fighter
    matrix[row][col] = normal_sign
    row, col = new_row, new_col

    command = input()

matrix_print(matrix)

