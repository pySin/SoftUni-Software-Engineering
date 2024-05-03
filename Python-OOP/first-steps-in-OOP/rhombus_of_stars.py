# # Rhombus Of Stars
#
#
# def find_positions(row_length, stars_number):
#     if stars_number % 2 != 0:
#         positions = [(row_length // 2) + 1]
#         for num in range(1, (stars_number // 2) + 1):
#             positions.append(positions[0] + (num * 2))
#             positions.append(positions[0] - (num * 2))
#     else:
#         positions = [((row_length // 2) + 1) - 1, ((row_length // 2) + 1) + 1]
#         for num in range(1, (stars_number // 2)):
#             positions.insert(0, positions[0] - 2)
#             positions.append(positions[-1] + 2)
#
#     return positions
#
#
# def build_line(i: int, n: int):
#     line = [" " for _ in range(n + (n - 1))]
#     positions = find_positions(len(line), i)
#     # print(positions)
#     for position in positions:
#         line[position - 1] = "*"
#     return line
#
#
# def display_rhombus(line: list):
#     for upper_line in range(len(line)):
#         print(" ".join(line[upper_line]))
#     for lower_line in range(len(line) - 2, - 1, - 1):
#         print(" ".join(line[lower_line]))
#
#
# n = int(input())
#
# lines = []
#
# for i in range(1, n + 1):
#     lines.append(build_line(i, n))
#
# display_rhombus(lines)

# Dian Kalaydjiev Solution


def print_row(n, row):
    print(" " * (n - row), end="")
    print(*["*"] * row)


def print_triangle(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_reverse_triangle(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def create_rhombus():
    n = int(input())
    print_triangle(n)
    print_reverse_triangle(n)


create_rhombus()
