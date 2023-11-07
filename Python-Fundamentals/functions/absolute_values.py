# Absolute Values

numbers = input()


def to_absolute(string_of_numbers):
    split_string = string_of_numbers.split(" ")
    list_positive = list(map(float, split_string))
    list_abs = list(map(abs, list_positive))
    print(list_abs)


to_absolute(numbers)
