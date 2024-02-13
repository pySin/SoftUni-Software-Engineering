# Flattening Matrix


def create_matrix(number_of_columns: int) -> list:
    matrix = []
    for _ in range(number_of_columns):
        column = [int(x) for x in input().split(", ")]
        matrix.append(column)
    return matrix


def flatten_matrix(matrix: list) -> list:
    matrix = [num for sublist in matrix for num in sublist]
    return matrix


def call_functions():
    number_of_columns = int(input())
    matrix = create_matrix(number_of_columns)
    flattened_matrix = flatten_matrix(matrix)
    print(flattened_matrix)


if __name__ == "__main__":
    call_functions()
