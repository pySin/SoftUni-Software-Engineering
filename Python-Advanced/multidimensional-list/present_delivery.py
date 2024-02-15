# Present Delivery


def create_matrix(size: int) -> list:
    matrix = [[x for x in input().split()] for _ in range(size)]
    return matrix


def movement(matrix: list, santa: tuple, size: int, presents: int, nice_k: int):

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1)
    }

    command = input()

    santa_horizontal = santa[0]
    santa_vertical = santa[1]
    while command != "Christmas morning":
        matrix[santa_horizontal][santa_vertical] = "-"
        santa_horizontal += directions[command][0]
        santa_vertical += directions[command][1]
        if matrix[santa_horizontal][santa_vertical] == "V":
            presents -= 1
            nice_k -= 1
            if presents == 0:
                matrix[santa_horizontal][santa_vertical] = "S"
                print("Santa ran out of presents!")
                return matrix, nice_k
            if nice_k == 0:
                matrix[santa_horizontal][santa_vertical] = "S"
                return matrix, nice_k
        elif matrix[santa_horizontal][santa_vertical] == "C":
            matrix[santa_horizontal][santa_vertical] = "S"
            for direction in directions:
                x_position = santa_horizontal + directions[direction][0]
                v_position = santa_vertical + directions[direction][1]
                if matrix[x_position][v_position] == "V":
                    matrix[x_position][v_position] = "-"
                    presents -= 1
                    nice_k -= 1
                    if presents == 0:
                        print("Santa ran out of presents!")
                        return matrix, nice_k
                    # if nice_k == 0:
                    #     return matrix, nice_k
                elif matrix[x_position][v_position] == "X":
                    matrix[x_position][v_position] = "-"
                    presents -= 1
                    if presents == 0:
                        print("Santa ran out of presents!")
                        return matrix, nice_k
            if nice_k == 0:
                return matrix, nice_k

        matrix[santa_horizontal][santa_vertical] = "S"
        command = input()

    return matrix, nice_k


def get_santa_position(matrix: list, size: int) -> tuple:
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "S":
                return i, j


def find_nice_kids(matrix: list) -> int:
    nice_kids = sum([sum([1 for x in row if x == "V"]) for row in matrix])
    return nice_kids


def call_functions():
    presents = int(input())
    size = int(input())
    matrix = create_matrix(size)
    # [print(row) for row in matrix]
    santa = get_santa_position(matrix, size)
    # print(santa)
    nice_kids = find_nice_kids(matrix)
    # print(f"Nice Kids: {nice_kids}")
    matrix, nice_k = movement(matrix, santa, size, presents, nice_kids)
    [print(*row) for row in matrix]
    if nice_k > 0:
        print(f"No presents for {nice_k} nice kid/s.")
    else:
        print(f"Good job, Santa! {nice_kids} happy nice kid/s.")


if __name__ == "__main__":
    call_functions()
