# Maximum edge of a triangle


def next_edge(side1, side2):
    return (side1 + side2) - 1


first_side = int(input())
second_side = int(input())

max_edge = next_edge(first_side, second_side)
print(max_edge)
