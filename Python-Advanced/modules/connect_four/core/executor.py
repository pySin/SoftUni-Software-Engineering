# Main Caller Function
from PythonAdvanced.modules.connect_four.core.valid_column import is_valid_column_choice
from PythonAdvanced.modules.connect_four.core.pick_cell import place_player_number
from PythonAdvanced.modules.connect_four.core.winner import is_winner
from PythonAdvanced.modules.connect_four.core.print_matrix import print_matrix


class FullColumnError(Exception):
    pass


def caller():
    ROWS = 6
    COLS = 7

    direction_mapper = [
        (-1, 0),  # Up
        (0, 1),  # Right
        (-1, 1),  # Up Right Diagonal
        (-1, -1),  # Up Left Diagonal
    ]

    matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    player = 1

    while True:
        try:
            selected_column_number = int(input(f"Player {player}, please choose a column: "))
            selected_column_index = selected_column_number - 1
            if not is_valid_column_choice(selected_column_index, COLS):
                raise ValueError
            current_row, current_col = place_player_number(selected_column_index, matrix, player, ROWS)
            print_matrix(matrix)
            if is_winner(current_row, current_col, matrix, player, direction_mapper, ROWS, COLS):
                print(f"Player {player} wins!")
                print_matrix(matrix)
                break
        except ValueError:
            print(f"Player {player}, please select number between 1 and {COLS}")
            continue
        except FullColumnError:
            print(f"Player {player}, this column is full, please select another one.")
            continue

        player += 1
        player = 2 if player % 2 == 0 else 1


caller()
