# Easter Bunny


def create_matrix(size: int) -> list:
    matrix = [[x for x in input().split()] for _ in range(size)]
    return matrix


def find_route(matrix: list, bunny: list, size: int) -> tuple:
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }

    top_direction = ""
    top_eggs = float("-inf")
    top_direction_steps = []
    for direction in directions:
        current_direction_eggs = 0
        current_direction_steps = []
        new_row = bunny[0]
        new_col = bunny[1]
        while True:
            new_row += directions[direction][0]
            new_col += directions[direction][1]
            if 0 <= new_row < size and 0 <= new_col < size:
                if matrix[new_row][new_col] != "X":
                    current_direction_steps.append([new_row, new_col])
                    current_direction_eggs += int(matrix[new_row][new_col])
                elif matrix[new_row][new_col] == "X":
                    break
                elif int(matrix[new_row][new_col]) < 0:
                    continue
            else:
                break

        if current_direction_eggs > top_eggs and current_direction_steps:
            top_eggs = current_direction_eggs
            top_direction = direction
            top_direction_steps = current_direction_steps
    return top_direction, top_eggs, top_direction_steps


def find_bunny(matrix: list, size: int) -> list:
    bunny = [[[row, col] for col in range(size) if matrix[row][col] == "B"] for row in range(size)]
    bunny = list(filter(lambda x: len(x) > 0, bunny))[0][0]
    return bunny


def call_functions():
    size = int(input())
    matrix = create_matrix(size)
    bunny = find_bunny(matrix, size)
    best_route = find_route(matrix, bunny, size)
    print(best_route[0])
    [print(x) for x in best_route[2]]
    print(best_route[1])


if __name__ == "__main__":
    call_functions()
