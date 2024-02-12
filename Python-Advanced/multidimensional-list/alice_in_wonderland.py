# Alice in wonderland


def create_matrix(size: int) -> list:
    matrix = [[x for x in input().split()] for _ in range(size)]
    return matrix


def find_alice(matrix: list, size: int) -> list:
    alice = [[[row, col] for col in range(size) if matrix[row][col] == "A"] for row in range(size)]
    alice = list(filter(lambda x: len(x) > 0, alice))[0][0]
    return alice


def alice_movement(matrix: list, position: list, size: int) -> tuple:
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    enough_tea_bags = 10
    tea_bags = 0
    is_party = False

    command = input()
    while command:
        matrix[position[0]][position[1]] = "*"
        position[0] += moves[command][0]
        position[1] += moves[command][1]

        if 0 <= position[0] < size and 0 <= position[1] < size:
            if matrix[position[0]][position[1]] == "R":
                matrix[position[0]][position[1]] = "*"
                break
            if matrix[position[0]][position[1]].isdigit():
                tea_bags += int(matrix[position[0]][position[1]])
                if tea_bags >= enough_tea_bags:
                    matrix[position[0]][position[1]] = "*"
                    is_party = True
                    break
        else:
            break
        command = input()

    return is_party, matrix


def call_functions():
    size = int(input())
    matrix = create_matrix(size)
    alice_position = find_alice(matrix, size)
    is_party, matrix = alice_movement(matrix, alice_position, size)
    if is_party:
        print("She did it! She went to the party.")
    else:
        print("Alice didn't make it to the tea party.")
    [print(*x) for x in matrix]


if __name__ == "__main__":
    call_functions()
