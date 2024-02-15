# # Miner
#
#
# def create_matrix() -> tuple:
#     size_square = int(input())
#     moves = input().split()
#     matrix = [[char for char in input().split()] for _ in range(size_square)]
#     return matrix, moves
#
#
# def turns(matrix: list, move: str, continuing: bool, start_position: list, coal: int) -> tuple:
#     if move == "up":
#         if start_position[0] - 1 < 0:
#             return matrix, continuing, start_position, coal
#         start_position[0] -= 1
#         if matrix[start_position[0]][start_position[1]] == "e":
#             continuing = False
#         if matrix[start_position[0]][start_position[1]] == "c":
#             coal += 1
#         matrix[start_position[0] + 1][start_position[1]] = "*"
#         matrix[start_position[0]][start_position[1]] = "s"
#     elif move == "right":
#         if start_position[1] + 1 > len(matrix) - 1:
#             return matrix, continuing, start_position, coal
#         start_position[1] += 1
#         if matrix[start_position[0]][start_position[1]] == "e":
#             continuing = False
#         if matrix[start_position[0]][start_position[1]] == "c":
#             coal += 1
#         matrix[start_position[0]][start_position[1] - 1] = "*"
#         matrix[start_position[0]][start_position[1]] = "s"
#     elif move == "down":
#         if start_position[0] + 1 > len(matrix) - 1:
#             return matrix, continuing, start_position, coal
#         start_position[0] += 1
#         if matrix[start_position[0]][start_position[1]] == "e":
#             continuing = False
#         if matrix[start_position[0]][start_position[1]] == "c":
#             coal += 1
#         matrix[start_position[0] - 1][start_position[1]] = "*"
#         matrix[start_position[0]][start_position[1]] = "s"
#     elif move == "left":
#         if start_position[1] - 1 < 0:
#             return matrix, continuing, start_position, coal
#         start_position[1] -= 1
#         if matrix[start_position[0]][start_position[1]] == "e":
#             continuing = False
#         if matrix[start_position[0]][start_position[1]] == "c":
#             coal += 1
#         matrix[start_position[0]][start_position[1] + 1] = "*"
#         matrix[start_position[0]][start_position[1]] = "s"
#     return matrix, continuing, start_position, coal
#
#
# def find_start_position(matrix: list) -> list:
#     start_position = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == "s":
#                 start_position.append(i)
#                 start_position.append(j)
#     return start_position
#
#
# def call_functions():
#     continuing = True
#     coal = 0
#     matrix, moves = create_matrix()
#     all_coal = sum([sum([1 for coal in row if coal == "c"]) for row in matrix])
#     # print(all_coal)
#     # print(moves)
#     # [print(row) for row in matrix]
#     start_position = find_start_position(matrix)
#     # print(start_position)
#     is_moves_over = False
#     for move in moves:
#         matrix, continuing, start_position, coal = turns(matrix, move, continuing, start_position, coal)
#         # print(f"Collected coal: {coal}")
#         # print("---------------------------")
#         # [print(row) for row in matrix]
#         if not continuing:
#             is_moves_over = True
#             print(f"Game over! {tuple(start_position)}")
#             break
#
#         if coal == all_coal:
#             is_moves_over = True
#             print(f"You collected all coal! {tuple(start_position)}")
#             break
#     if not is_moves_over:
#         remaining_coal = all_coal - coal
#         print(f"{remaining_coal} pieces of coal left. {tuple(start_position)}")
#
#
# if __name__ == "__main__":
#     call_functions()


# Atanas Atanasov's solution

def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())
commands = input().split()

matrix = []
curr_row, curr_coll = 0, 0
coal = 0
game_over = False

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "s":
            curr_row, curr_coll = r, c
        elif matrix[r][c] == "c":
            coal += 1

for command in commands:
    if command == "up":
        if is_valid(curr_row - 1, curr_coll, n):
            curr_row -= 1
    if command == "down":
        if is_valid(curr_row + 1, curr_coll, n):
            curr_row += 1
    if command == "left":
        if is_valid(curr_row, curr_coll - 1, n):
            curr_coll -= 1
    if command == "right":
        if is_valid(curr_row, curr_coll + 1, n):
            curr_coll += 1

    if matrix[curr_row][curr_coll] == "e":
        print(f"Game over! ({curr_row}, {curr_coll})")
        game_over = True
        break
    elif matrix[curr_row][curr_coll] == "c":
        coal -= 1
        matrix[curr_row][curr_coll] = "*"
        if coal == 0:
            print(f"You collected all coal! ({curr_row}, {curr_coll})")
            game_over = True
            break

if not game_over:
    print(f"{coal} pieces of coal left. ({curr_row}, {curr_coll})")


