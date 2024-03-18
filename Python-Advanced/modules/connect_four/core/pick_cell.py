class FullColumnError(Exception):
    pass

def place_player_number(column_index, matrix, player_number, rows):
    selected_row_index = None
    for row_index in range(rows-1, -1, -1):
        if matrix[row_index][column_index] == 0:
            selected_row_index = row_index
            break
    if selected_row_index is None:
        raise FullColumnError
    matrix[selected_row_index][column_index] = player_number
    return selected_row_index, column_index