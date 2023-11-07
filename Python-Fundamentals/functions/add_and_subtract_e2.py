# Add and Subtract

num1 = int(input())
num2 = int(input())
num3 = int(input())


def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(result, third_number):
    return result - third_number


def add_and_subtract(first_number, second_number, third_number):
    sum_result = sum_numbers(first_number, second_number)
    final_result = sum_result - third_number
    return final_result


result_number = add_and_subtract(num1, num2, num3)
print(result_number)
