# Connect Four / Ines

ROWS = 6
COLS = 7

direction_mapper = [
    (-1, 0),  # Up
    # (1, 0),  # Down
    (0, 1),  # Right
    # (0, -1),  # Left
    (-1, 1),  # Up Right Diagonal
    # (1, -1),  # Down Left Diagonal
    (-1, -1),  # Up Left Diagonal
    # (1, 1)  # Down Right Diagonal
]


class FullColumnError(Exception):
    pass


def print_matrix(matrix):
    for row in matrix:
        print(row)


def is_valid_column_choice(selected_column_index):
    if 0 <= selected_column_index < COLS:
        return True
    return False


def place_player_number(column_index, matrix, player_number):
    selected_row_index = None
    for row_index in range(ROWS-1, -1, -1):
        if matrix[row_index][column_index] == 0:
            selected_row_index = row_index
            break
    if selected_row_index is None:
        raise FullColumnError
    matrix[selected_row_index][column_index] = player_number
    return selected_row_index, column_index


def is_valid_place(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return True
    return False


def requested_direction_count(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row + row_movement * i
        col_index_to_check = current_col + col_movement * i

        if not is_valid_place(row_index_to_check, col_index_to_check):
            break

        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count


def opposite_direction_count(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_movement * i
        col_index_to_check = current_col - col_movement * i

        if not is_valid_place(row_index_to_check, col_index_to_check):
            break

        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count


def is_winner(current_row, current_col, matrix, player):
    for row_movement, col_movement in direction_mapper:
        count_direction = requested_direction_count(current_row, current_col, row_movement,
                                                       col_movement, matrix, player)
        count_opposite_direction = opposite_direction_count(current_row, current_col, row_movement,
                                                       col_movement, matrix, player)
        if (count_direction + count_opposite_direction) >= 3:
            return True
    return False


matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

player = 1
while True:
    try:
        selected_column_number = int(input(f"Player {player}, please choose a column: "))
        selected_column_index = selected_column_number - 1
        if not is_valid_column_choice(selected_column_index):
            raise ValueError
        current_row, current_col = place_player_number(selected_column_index, matrix, player)  # it
        # raises an error in here and the exceptions down have to catch it!
        if is_winner(current_row, current_col, matrix, player):
            print(f"Player {player} wins!")
            print_matrix(matrix)
            break
        print_matrix(matrix)
    except ValueError:
        print(f"Player {player }, please select number between 1 and {COLS}")
        continue
    except FullColumnError:
        print(f"Player {player}, this column is full, please select another one.")
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1
