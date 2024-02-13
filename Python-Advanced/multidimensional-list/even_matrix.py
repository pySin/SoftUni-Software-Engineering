# Even Matrix


def create_matrix(shape: int) -> list:

    matrix = []
    for row in range(shape):
        line = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
        matrix.append(line)
    return matrix


def call_functions():
    matrix_square_shape = int(input())
    matrix = create_matrix(matrix_square_shape)
    print(matrix)


if __name__ == "__main__":
    call_functions()
