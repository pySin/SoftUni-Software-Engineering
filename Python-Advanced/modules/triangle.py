# Triangle


def create_triangle(n):
    for i in range(n):
        [print(f"{j} ", end="") for j in range(i)]
        print()

    for i in range(n, 0, - 1):
        [print(f"{j} ", end="") for j in range(i)]
        print()

