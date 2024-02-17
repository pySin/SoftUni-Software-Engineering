# # Range day
#
#
# def create_matrix(size: int) -> list:
#     matrix = [[x for x in input().split()] for _ in range(size)]
#     return matrix
#
#
# def find_player(matrix: list, size: int) -> list:
#     shooter = [[[row, col] for col in range(size) if matrix[row][col] == "A"] for row in range(size)]
#     shooter = list(filter(lambda x: len(x) > 0, shooter))[0][0]
#     return shooter
#
#
# def find_targets(matrix: list) -> int:
#     targets = sum([row.count("x") for row in matrix])
#     return targets
#
#
# def move_or_shoot(matrix: list, number_of_commands: int, shooter: list, size: int, targets: int) -> tuple:
#
#     directions = {
#         "right": (0, 1),
#         "left": (0, -1),
#         "up": (-1, 0),
#         "down": (1, 0)
#     }
#
#     targets_hit = []
#     for _ in range(number_of_commands):
#         command = input().split()
#         action = command[0]
#         direction = command[1]
#
#         if action == "move":
#             for i in range(int(command[2])):
#                 shooter[0] += directions[direction][0]
#                 shooter[1] += directions[direction][1]
#                 if 0 <= shooter[0] < size and 0 <= shooter[1] < size:
#                     if matrix[shooter[0]][shooter[1]] != "x":
#                         matrix[shooter[0]][shooter[1]] = "A"
#                         matrix[shooter[0] - directions[direction][0]][shooter[1] - directions[direction][1]] = "."
#                 else:
#                     shooter[0] -= directions[direction][0]
#                     shooter[1] -= directions[direction][1]
#                     break
#         elif action == "shoot":
#             bullet_x = shooter[0]
#             bullet_y = shooter[1]
#             while True:
#                 bullet_x += directions[direction][0]
#                 bullet_y += directions[direction][1]
#                 if 0 <= bullet_x < size and 0 <= bullet_y < size:
#                     if matrix[bullet_x][bullet_y] == "x":
#                         targets_hit.append([bullet_x, bullet_y])
#                         targets -= 1
#                         matrix[bullet_x][bullet_y] = "."
#                         break
#                 else:
#                     break
#
#             if targets == 0:
#                 return matrix, targets, targets_hit
#
#     return matrix, targets, targets_hit
#
#
# def call_functions():
#     size = 5
#     matrix = create_matrix(size)
#     shooter = find_player(matrix, size)
#     number_of_commands = int(input())
#     initial_targets = find_targets(matrix)
#     matrix, targets, targets_hit = move_or_shoot(matrix, number_of_commands, shooter, size, initial_targets)
#
#     if targets == 0:
#         print(f"Training completed! All {initial_targets} targets hit.")
#     else:
#         print(f"Training not completed! {targets} targets left.")
#     [print(x) for x in targets_hit]
#
#
# if __name__ == "__main__":
#     call_functions()

# -- Atanas Atanasov's solution

matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}
targets_down = []

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "shoot":
        r = my_position[0] + directions[command[1]][0]
        c = my_position[1] + directions[command[1]][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == "x":
                targets -= 1
                targets_down.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == "move":

        #     steps = int(command[2])
        #     direction = command[1]
        #     if direction == "up":
        #         r = my_position[0] - steps
        #         c = my_position[1]
        #     elif direction == "down":
        #         r = my_position[0] + steps
        #         c = my_position[1]
        #     elif direction == "left":
        #         r = my_position[0]
        #         c = my_position[1] - steps
        #     else:
        #         r = my_position[0]
        #         c = my_position[1] + steps
        r = my_position[0] + directions[command[1]][0] * int(command[2])
        c = my_position[1] = directions[command[1]][1] * int(command[2])

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_down]
