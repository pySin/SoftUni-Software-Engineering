# Sum Metrix Columns


def create_matrix() -> list:
    rows, cols = [int(x) for x in input().split(", ")]
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    return matrix


def display_sums(matrix: list) -> list:
    new_cols = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    [print(sum(row)) for row in new_cols]
    return new_cols


def call_functions():
    matrix = create_matrix()
    display_sums(matrix)


if __name__ == "__main__":
    call_functions()
