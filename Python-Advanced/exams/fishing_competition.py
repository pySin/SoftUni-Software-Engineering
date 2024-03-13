# Fishing  Competition


def get_matrix(n: int) -> list:
    matrix = [list(input()) for _ in range(n)]
    # matrix = [input().split("") for _ in range(n)]
    return matrix


def get_current_position(matrix: list, char: str) -> tuple:
    position = None
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == char:
                position = i, j
    return position


def up(current_row: int, current_col: int):
    new_row = current_row - 1
    new_col = current_col
    return new_row, new_col


def down(current_row: int, current_col: int):
    # print("In DOWN:", current_row, current_col)
    new_row = current_row + 1
    new_col = current_col
    # print("In DOWN_2:", current_row, current_col)
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


def call_functions():
    quota = 20
    n = int(input())
    matrix = get_matrix(n)
    player_symbol = "S"
    row, col = get_current_position(matrix, player_symbol)

    fish_caught = 0
    command = input()
    while command != "collect the nets":
        if command == "up":
            new_row, new_col = up(row, col)
            if not boundary_check(matrix, new_row, new_col):
                new_row = len(matrix) - 1

            if matrix[new_row][new_col] == "W":
                print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                      f"Last coordinates of the ship: [{new_row},{new_col}]")
                return
            elif matrix[new_row][new_col].isdigit():
                fish_caught += int(matrix[new_row][new_col])
            matrix[row][col] = "-"
            row, col = new_row, new_col
            matrix[row][col] = "S"
        if command == "down":
            new_row, new_col = down(row, col)
            # print("In call:", new_row, new_col)
            if not boundary_check(matrix, new_row, new_col):
                new_row = 0

            if matrix[new_row][new_col] == "W":
                print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                      f"Last coordinates of the ship: [{new_row},{new_col}]")
                return
            elif matrix[new_row][new_col].isdigit():
                fish_caught += int(matrix[new_row][new_col])
            matrix[row][col] = "-"
            row, col = new_row, new_col
            matrix[row][col] = "S"
        if command == "right":
            new_row, new_col = right(row, col)
            # print("In call:", new_row, new_col)
            if not boundary_check(matrix, new_row, new_col):
                new_col = 0

            if matrix[new_row][new_col] == "W":
                print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                      f"Last coordinates of the ship: [{new_row},{new_col}]")
                return
            elif matrix[new_row][new_col].isdigit():
                fish_caught += int(matrix[new_row][new_col])
            matrix[row][col] = "-"
            row, col = new_row, new_col
            matrix[row][col] = "S"
        if command == "left":
            new_row, new_col = left(row, col)
            # print("In call:", new_row, new_col)
            if not boundary_check(matrix, new_row, new_col):
                new_col = len(matrix) - 1

            if matrix[new_row][new_col] == "W":
                print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                      f"Last coordinates of the ship: [{new_row},{new_col}]")
                return
            elif matrix[new_row][new_col].isdigit():
                fish_caught += int(matrix[new_row][new_col])
            matrix[row][col] = "-"
            row, col = new_row, new_col
            matrix[row][col] = "S"

        command = input()

    if fish_caught >= quota:
        print(f"Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {quota - fish_caught} "
              f"tons of fish more.")
    if fish_caught > 0:
        print(f"Amount of fish caught: {fish_caught} tons.")

    for m_row in matrix:
        print("".join(m_row))


if __name__ == "__main__":
    call_functions()
