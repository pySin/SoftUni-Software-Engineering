# Symbol in matrix


def get_matrix():
    n = int(input())
    matrix = [[x for x in list(input())] for _ in range(n)]
    return matrix


def call_functions():
    matrix = get_matrix()
    symbol = input()
    is_symbol = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == symbol:
                print(f"({i}, {j})")
                is_symbol = True
                break
        if is_symbol:
            break

    if not is_symbol:
        print(f"{symbol} does not occur in the matrix")


if __name__ == "__main__":
    call_functions()
