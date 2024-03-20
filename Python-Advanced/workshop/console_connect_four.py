# Console Connect Four


def if_game_over(matrix: list, row: int, column: int) -> bool:
    player = matrix[row][column]
    links = 0

    # Vertical Check
    for down_row in range(row, len(matrix)):
        if matrix[down_row][column] == player:
            links += 1
            if links == 4:
                return True
        else:
            links = 0
        if down_row == len(matrix) - 1:
            links = 0

    # Horizontal Check
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == player:
                links += 1
                if links == 4:
                    return True
                if j == len(matrix[0]) - 1:
                    links = 0
            elif j == len(matrix[0]) - 1:
                links = 0
            else:
                links = 0

    # Diagonal Check
    for i in range(1, len(matrix)):
        if 0 <= row - i < len(matrix) and 0 <= column - i < len(matrix[0]):
            if matrix[row - i][column - i] == player:
                links += 1
                if links + 1 == 4:
                    print("Upper Left Diagonal")
                    return True
            else:
                break
        else:
            break
    for i in range(1, len(matrix)):
        if 0 <= row + i < len(matrix) and 0 <= column + i < len(matrix[0]):
            if matrix[row + i][column + i] == player:
                links += 1
                if links + 1 == 4:
                    print("Lower Right Diagonal")
                    return True
            else:
                links = 0
                break
        else:
            links = 0
            break

    for i in range(1, len(matrix)):
        if 0 <= row + i < len(matrix) and 0 <= column - i < len(matrix[0]):
            if matrix[row + i][column - i] == player:
                links += 1
                if links + 1 == 4:
                    print("Lower Left Diagonal")
                    return True
            else:
                break
        else:
            break

    for i in range(1, len(matrix)):
        if 0 <= row - i < len(matrix) and 0 <= column + i < len(matrix[0]):
            if matrix[row - i][column + i] == player:
                links += 1
                if links + 1 == 4:
                    return True
            else:
                break
        else:
            break

    return False


def call_functions():
    matrix = [[0 for _ in range(7)] for _ in range(6)]

    player_1 = [1, 0]
    player_2 = [2, 0]

    is_game_over = False
    moves = 1
    while True:
        if moves % 2 != 0:
            current_player = player_1
        else:
            current_player = player_2

        try:
            current_column = int(input(f"Player {current_player[0]}, please choose a column: "))
            if not 0 < current_column <= len(matrix[0]):
                print(f"Choose a number bigger than 0 and smaller than {len(matrix[0]) + 1}")
                continue
            moves += 1
            for i in range(len(matrix) - 1, - 1, - 1):
                if matrix[i][current_column - 1] == 0:
                    matrix[i][current_column - 1] = current_player[0]
                    is_game_over = if_game_over(matrix, i, current_column - 1)
                    break
        except ValueError:
            print("You must insert a number!")
            continue
        for row in matrix:
            print(row)

        if is_game_over:
            print(f"Player {current_player[0]} wins!")
            break


if __name__ == "__main__":
    call_functions()
