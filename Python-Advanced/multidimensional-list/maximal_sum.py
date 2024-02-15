# Maximal Sum
import sys


def get_matrix() -> list:
    rows, cols = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    return matrix


def check_square(matrix: list, i: int, j: int, square_size: int) -> tuple:
    square = []
    for row in range(square_size):
        square.append(matrix[i + row][j: j + square_size])

    current_sum = sum([sum(x) for x in square])
    return current_sum, square


def max_squares(matrix: list, square_size: int) -> tuple:
    top_square = 0
    top_sum = -sys.maxsize

    for i in range(len(matrix) - (square_size - 1)):
        for j in range(len(matrix[0]) - (square_size - 1)):
            current_sum, current_square = check_square(matrix, i, j, square_size)
            if current_sum > top_sum:
                top_sum = current_sum
                top_square = current_square

    return top_sum, top_square


def call_functions():
    square_size = 3
    matrix = get_matrix()
    top_sum, top_square = max_squares(matrix, square_size)
    print(f"Sum = {top_sum}")
    if type(top_square) == list:
        for row in top_square:
            print(*row)
    else:
        print(top_square)


if __name__ == "__main__":
    call_functions()
