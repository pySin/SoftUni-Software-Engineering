# Even Or Odd


def even_odd(*args):
    command = args[-1]
    numbers = [int(x) for x in args[:-1]]
    result = None
    if command == "even":
        result = list(filter(lambda x: x % 2 == 0, numbers))
    elif command == "odd":
        result = list(filter(lambda x: x if x % 2 != 0 else False, numbers))
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
