from PythonAdvanced.modules.connect_four.core.valid_place import is_valid_place


def requested_direction_count(current_row, current_col, row_movement, col_movement, matrix, player, rows, cols):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row + row_movement * i
        col_index_to_check = current_col + col_movement * i

        if not is_valid_place(row_index_to_check, col_index_to_check, rows, cols):
            break

        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count


def opposite_direction_count(current_row, current_col, row_movement, col_movement, matrix, player, rows, cols):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_movement * i
        col_index_to_check = current_col - col_movement * i

        if not is_valid_place(row_index_to_check, col_index_to_check, rows, cols):
            break

        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count