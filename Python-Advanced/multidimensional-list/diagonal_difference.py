# Diagonal Difference


def get_matrix() -> list:
    square_size = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(square_size)]
    return matrix


def get_diagonals(matrix: list) -> tuple:
    first_diagonal = [matrix[i][i] for i in range(len(matrix))]
    second_diagonal = [matrix[i][(len(matrix) - 1) - i] for i in range(len(matrix))]
    return first_diagonal, second_diagonal


def call_functions():
    matrix = get_matrix()
    first_diagonal, second_diagonal = get_diagonals(matrix)
    print(abs(sum(first_diagonal) - sum(second_diagonal)))


if __name__ == "__main__":
    call_functions()

