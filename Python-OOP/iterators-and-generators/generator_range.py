# Generator Range


def genrange(start: int, end: int):

    while start <= end:
        yield start
        start += 1


print(genrange(1, 10))
print(list(genrange(1, 10)))
