# Knight Game


# def create_matrix(size: int) -> list:
#     matrix = [[x for x in list(input())] for _ in range(size)]
#     return matrix
#
#
# def find_k_positions(matrix: list) -> list:
#     k_positions = []
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             if matrix[row][col] == "K":
#                 k_positions.append([row, col, []])
#     return k_positions
#
#
# def hits_by_position(matrix: list, k_positions: list, size: int) -> list:
#
#     for position in range(len(k_positions)):
#         row = k_positions[position][0]
#         col = k_positions[position][1]
#         # Check upper moves
#         if row - 2 in range(size):
#             if col - 1 in range(size):
#                 if matrix[row - 2][col - 1] == "K":
#                     k_positions[position][2].append([row - 2, col - 1])
#             if col + 1 in range(size):
#                 if matrix[row - 2][col + 1] == "K":
#                     k_positions[position][2].append([row - 2, col + 1])
#
#         # Check lower moves
#         if row + 2 in range(size):
#             if col - 1 in range(size):
#                 if matrix[row + 2][col - 1] == "K":
#                     k_positions[position][2].append([row + 2, col - 1])
#             if col + 1 in range(size):
#                 if matrix[row + 2][col + 1] == "K":
#                     k_positions[position][2].append([row + 2, col + 1])
#
#         # Check left moves
#         if col - 2 in range(size):
#             if row - 1 in range(size):
#                 if matrix[row - 1][col - 2] == "K":
#                     k_positions[position][2].append([row - 1, col - 2])
#             if row + 1 in range(size):
#                 if matrix[row + 1][col - 2] == "K":
#                     k_positions[position][2].append([row + 1, col - 2])
#
#         # Check right moves
#         if col + 2 in range(size):
#             if row - 1 in range(size):
#                 if matrix[row - 1][col + 2] == "K":
#                     k_positions[position][2].append([row - 1, col + 2])
#             if row + 1 in range(size):
#                 if matrix[row + 1][col + 2] == "K":
#                     k_positions[position][2].append([row + 1, col + 2])
#
#     return k_positions
#
#
# def find_maximum_hits(position_hits: list) -> int:
#     maximum_hits = [len(x[2]) for x in position_hits]
#     return max(maximum_hits)
#
#
# def remove_maximum_hits_matrix_position(matrix: list, position_hits: list, maximum_hits: int) -> list:
#
#     for position in position_hits:
#         if len(position[2]) == maximum_hits:
#             matrix[position[0]][position[1]] = "0"
#             break
#     return matrix
#
#
# def call_functions():
#     size = int(input())
#     removed_matrix_positions = 0
#     matrix = create_matrix(size)
#     k_positions = find_k_positions(matrix)
#     position_hits = hits_by_position(matrix, k_positions, size)
#     maximum_hits = find_maximum_hits(position_hits)
#     while maximum_hits != 0:
#         matrix = remove_maximum_hits_matrix_position(matrix, position_hits, maximum_hits)
#         removed_matrix_positions += 1
#         k_positions = find_k_positions(matrix)
#         position_hits = hits_by_position(matrix, k_positions, size)
#         maximum_hits = find_maximum_hits(position_hits)
#     print(removed_matrix_positions)
#
#
# if __name__ == "__main__":
#     call_functions()

# Atanas Atanasov's Solution

n = int(input())

matrix = []
knights = []

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if matrix[new_row][new_col] == "K":
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
