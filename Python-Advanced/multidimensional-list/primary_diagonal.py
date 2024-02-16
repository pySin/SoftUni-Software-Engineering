# Primary Diagonal


def create_matrix() -> list:
    size = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size)]
    return matrix


def diagonal_sum(matrix: list) -> list:
    diagonal = sum([matrix[x][x] for x in range(len(matrix))])
    return diagonal


def call_functions():
    matrix = create_matrix()
    diagonal = diagonal_sum(matrix)
    print(diagonal)


if __name__ == "__main__":
    call_functions()
