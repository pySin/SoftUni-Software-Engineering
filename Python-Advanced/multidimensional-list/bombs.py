# Bombs


def row_first_blast(matrix: list, row: int, column: int, length: int, blast_value: int):
    if row == 0:
        if column == 0:
            for i in range(row + 2):
                for j in range(column + 2):
                    if matrix[i][j] > 0:
                        matrix[i][j] -= blast_value
        elif column == length - 1:
            for i in range(row + 2):
                for j in range(length - 2, length):
                    if matrix[i][j] > 0:
                        matrix[i][j] -= blast_value
        else:
            for i in range(row + 2):
                for j in range(column - 1, column + 2):
                    if matrix[i][j] > 0:
                        matrix[i][j] -= blast_value
    return matrix


def column_last_blast(matrix: list, row: int, column: int, length: int, blast_value: int):
    if row == length - 1:
        for i in range(row - 1, row + 1):
            for j in range(column - 1, column + 1):
                if matrix[i][j] > 0:
                    matrix[i][j] -= blast_value
    else:
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 1):
                if matrix[i][j] > 0:
                    matrix[i][j] -= blast_value
    return matrix


def row_last_blast(matrix: list, row: int, column: int, length: int, blast_value: int):
    if column == 0:
        for i in range(row - 1, row + 1):
            for j in range(column, column + 2):
                if matrix[i][j] > 0:
                    matrix[i][j] -= blast_value
    else:
        for i in range(row - 1, row + 1):
            for j in range(column - 1, column + 2):
                if matrix[i][j] > 0:
                    matrix[i][j] -= blast_value
    return matrix


def column_first_blast(matrix: list, row: int, column: int, length: int, blast_value: int):
    for i in range(row - 1, row + 2):
        for j in range(column, column + 2):
            if matrix[i][j] > 0:
                matrix[i][j] -= blast_value
    return matrix


def inside_blast(matrix: list, row: int, column: int, length: int, blast_value: int):
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if matrix[i][j] > 0:
                matrix[i][j] -= blast_value
    return matrix


def detonate_bomb(matrix: list, bomb: str, length: int):
    row, column = [int(x) for x in bomb.split(",")]
    blast_value = matrix[row][column]
    if row == 0:
        matrix = row_first_blast(matrix, row, column, length, blast_value)
    elif column == length - 1:
        matrix = column_last_blast(matrix, row, column, length, blast_value)
    elif row == length - 1:
        matrix = row_last_blast(matrix, row, column, length, blast_value)
    elif column == 0:
        matrix = column_first_blast(matrix, row, column, length, blast_value)
    else:
        matrix = inside_blast(matrix, row, column, length, blast_value)

    return matrix


def display_matrix(matrix: list, square: int):
    alive_cells = 0
    cells_sum = 0
    for i in range(square):
        for j in range(square):
            if matrix[i][j] > 0:
                alive_cells += 1
                cells_sum += matrix[i][j]
    print(f"Alive cells: {alive_cells}")
    print(f"Sum: {cells_sum}")
    [print(*row) for row in matrix]


def call_functions():
    square_rc = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(square_rc)]
    bombs = input().split()
    for bomb in bombs:
        matrix = detonate_bomb(matrix, bomb, square_rc)

    display_matrix(matrix, square_rc)


if __name__ == "__main__":
    call_functions()
