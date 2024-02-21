# Square With maximum Sum


def create_matrix(rows: int) -> list:
    matrix = [[int(num) for num in input().split(", ")] for _ in range(rows)]
    return matrix


def find_square_sum(matrix: list) -> tuple:
    top_result = 0
    top_square = []

    for row in range(len(matrix) - 1):
        for col in range(len(matrix[0]) - 1):
            first_number = matrix[row][col]
            second_number = matrix[row][col + 1]
            third_number = matrix[row + 1][col]
            forth_number = matrix[row + 1][col + 1]
            current_square_result = first_number + second_number + third_number + forth_number
            if current_square_result > top_result:
                top_result = current_square_result
                top_square = [[first_number, second_number], [third_number, forth_number]]
    return top_result, top_square


def call_functions():
    rows, cols = [int(x) for x in input().split(", ")]
    matrix = create_matrix(rows)
    top_result, top_square = find_square_sum(matrix)
    for square_line in top_square:
        print(*square_line)
    print(top_result)


if __name__ == "__main__":
    call_functions()
