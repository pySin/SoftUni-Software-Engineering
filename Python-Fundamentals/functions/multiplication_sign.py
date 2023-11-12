# Multiplication sign


def numbers_and_signs():
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())

    if number_1 == 0 or number_2 == 0 or number_3 == 0:
        return "zero"

    negative_numbers = []

    if number_1 < 0:
        negative_numbers.append("negative")
    else:
        negative_numbers.append("positive")

    if number_2 < 0:
        negative_numbers.append("negative")
    else:
        negative_numbers.append("positive")

    if number_3 < 0:
        negative_numbers.append("negative")
    else:
        negative_numbers.append("positive")

    if negative_numbers.count("negative") == 1 or negative_numbers.count("negative") == 3:
        return "negative"
    else:
        return "positive"


def call_functions():
    result = numbers_and_signs()
    return result


if __name__ == "__main__":
    plus_minus = call_functions()
    print(plus_minus)
