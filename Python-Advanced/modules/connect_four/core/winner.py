from PythonAdvanced.modules.connect_four.core.diagonal_directions import requested_direction_count, \
    opposite_direction_count

def is_winner(current_row, current_col, matrix, player, direction_mapper, rows, cols):
    for row_movement, col_movement in direction_mapper:
        count_direction = requested_direction_count(current_row, current_col, row_movement,
                                                       col_movement, matrix, player, rows, cols)
        count_opposite_direction = opposite_direction_count(current_row, current_col, row_movement,
                                                       col_movement, matrix, player, rows, cols)
        if (count_direction + count_opposite_direction) >= 3:
            return True
    return False