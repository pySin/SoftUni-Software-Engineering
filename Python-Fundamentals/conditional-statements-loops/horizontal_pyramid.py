# Horizontal Pyramid

half_line_length = int(input())

for i in range(half_line_length):
    for j in range(half_line_length - i):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    for j in range(half_line_length - i):
        print(" ", end="")
    print()


for i in range(half_line_length, -1, -1):
    for j in range(half_line_length - i):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    for j in range(half_line_length - i):
        print(" ", end="")
    print()
