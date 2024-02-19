# Square Matrix 2 x 2


def get_matrix() -> list:
    rows, cols = [int(x) for x in input().split()]
    matrix = [[x for x in input().split()] for _ in range(rows)]
    return matrix


def find_squares(matrix: list) -> int:
    squares = 0

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            current_position = matrix[i][j]
            if current_position == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                squares += 1
    return squares


def call_functions():
    matrix = get_matrix()
    squares = find_squares(matrix)
    print(squares)


if __name__ == "__main__":
    call_functions()
