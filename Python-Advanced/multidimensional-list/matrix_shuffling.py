# Matrix Shuffling


def get_matrix() -> list:
    rows, cols = [int(x) for x in input().split()]
    matrix = [[x for x in input().split()] for _ in range(rows)]
    return matrix


def call_functions():
    matrix = get_matrix()

    command = input()

    while command != "END":
        instructions = command.split()
        action = instructions[0]

        if action == "swap" and len(instructions) == 5:
            row_1, col_1, row_2, col_2 = [int(x) for x in instructions[1:]]

            # print("Coordinates")
            if col_1 <= len(matrix[0]) - 1 and col_2 <= len(matrix[0]) - 1 and \
                    row_1 <= len(matrix) - 1 and row_2 <= len(matrix) - 1:
                # print("In Comparison")
                matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
                for row in matrix:
                    print(*row)
            else:
                # print("Inner Invalid")
                print("Invalid input!")
        else:
            print("Invalid input!")

        command = input()


if __name__ == "__main__":
    call_functions()
