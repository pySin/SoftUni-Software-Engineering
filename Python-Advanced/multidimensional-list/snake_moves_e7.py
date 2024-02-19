# Snake Moves
from collections import deque


def create_matrix(rows: int, cols: int, snake_string: str):
    snake_string = deque(snake_string)
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            if (i + 1) % 2 != 0:
                matrix[i].append(snake_string[0])
                snake_string.rotate(-1)
            else:
                matrix[i].insert(0, snake_string[0])
                snake_string.rotate(-1)
    return matrix


def call_functions():
    rows, cols = [int(x) for x in input().split()]
    snake_string = input()
    matrix = create_matrix(rows, cols, snake_string)
    [print("".join(row)) for row in matrix]


if __name__ == "__main__":
    call_functions()
