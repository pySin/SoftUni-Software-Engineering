# Recursive Power


def recursive_power(number: int, power: int):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)


# print(recursive_power(10, 100))
print(recursive_power(10, 5))
