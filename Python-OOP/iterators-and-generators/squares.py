# Squares


def squares(n):
    num = 1
    while n >= num:
        yield num * num
        num += 1


for sq in squares(5):
    print(sq)
