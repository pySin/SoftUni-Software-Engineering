# Multidimensional Lists Tests / Matrix


# matrix = [[1, 2, 3],
#     [4, 5, 6]
#     ]
#
# print(matrix[1][2])
# matrix[0][1] = 100
# print(matrix)

# --

# matrix = []
#
# rows_count = 2
# cols_count = 3
#
# for row in range(rows_count):
#     matrix.append([1, 2, 3])
#
# print(matrix[0])
# print(matrix[1])

# -- Creating multidimensional lists

# matrix = []
#
# rows_count = 2
# cols_count = 3
#
#
# number = 1
# for row in range(rows_count):
#     matrix.append([])
#     for col in range(cols_count):
#         matrix[row].append(number)
#         number += 1
#
# print(matrix)

# --

# matrix = [[x + y for y in range(4)] for x in range(5)]
# for row in matrix:
#     print(row)

# -- Flattening a matrix

# matrix = [[1, 2, 3], [4, 5, 6]]
# flattened = [num for sublist in matrix for num in sublist]
# num_flat = [matrix[inner][i] for inner in range(len(matrix)) for i in range(len(matrix[inner]))]
# print(num_flat)
# # flattened = []
# # for i in range(len(matrix)):
# #     for j in range(len(matrix[i])):
# #         flattened.append(matrix[i][j])
#
# print(flattened)

# - Double Loop Comprehension

# double_loop = [second_num for first_num in range(3) for second_num in range(4)]
# print(double_loop)


# Traversing elements with list comprehension

# matrix = [[1, 2, 3], [4, 5, 6]]
# nums = [num for num in [j for j in matrix]]
# print(nums)

# -- Backwards diagonal

# def create_matrix() -> list:
#     size = int(input())
#     matrix = [[int(x) for x in input().split()] for _ in range(size)]
#     return matrix
#
#
# matrix = create_matrix()
# diagonal_sum = 0
# for row in range(len(matrix) - 1, - 1, - 1):
#     diagonal_sum += matrix[row][row]
# print(diagonal_sum)

# -- Usage of "exit()"

# list_1 = [1, 2, 3, 4, 5]
# print(list_1)
# exit()
# print(list_1[::-1])  # Unreachable code

# -- comprehension result multiplication

# size = int(input())
# matrix = [[0] * size for row in range(0, size)]
# print(matrix)
# print([1] * 3)

# -- negative variable index

# x = 2
# list_1 = [1, 2, 3, 4, 5]
# print(list_1[-x])

# -- matrix print

# matrichina = [
#     [1, 2],
#     [3, 4]
# ]
#
# [[print(x, end="") for x in row] for row in matrichina]

# rows = 4
# row = 3
# col = 3
#
# if 0 <= row < rows or 0 <= col < rows:
#     print(row)
# if row < 0 or row >= rows or col < 0 or col >= rows

# --

# x = -2
# z = 3
# d = x + z
# print(d)

# --

# z = []
# print("a")
# [print(x) for x in z]
# print("b")

# -- Flattening a list

# two_d_list = [[1, 2, 3], [4, 5, 6]]
# flattened_list = [el for i_list in two_d_list for el in i_list]
# print(flattened_list)

# deque test

# from collections import deque
#
# phrase = "hello"
# phrase = deque(phrase)
# print(phrase)

print(0 % 2)

