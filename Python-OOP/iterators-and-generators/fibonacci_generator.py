# Fibonacci Generator


def fibonacci():

    previous_number = 0
    current_number = 1
    yield previous_number
    yield current_number

    while True:
        yield previous_number + current_number
        new_current = previous_number + current_number
        previous_number = current_number
        current_number = new_current


# generator = fibonacci()
# for i in range(5):
#     print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
