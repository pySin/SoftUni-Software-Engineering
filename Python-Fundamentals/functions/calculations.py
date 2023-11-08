# Calculations

# def operations(math_operation, number_1, number_2):
#     if math_operation == "multiply":
#         return number_1 * number_2
#     if math_operation == "divide":
#         return number_1 / number_2
#     if math_operation == "add":
#         return number_1 + number_2
#     if math_operation == "subtract":
#         return number_1 - number_2


def math_operations(operator, num1, num2):
    return {
        "multiply": num1 * num2,
        "divide": int(num1 / num2),
        "add": num1 + num2,
        "subtract": num1 - num2
    }.get(operator, "Invalid Operator")


operation = input()  # "multiply", "divide", "add", "subtract".
first_operand = int(input())
second_operand = int(input())

result = math_operations(operation, first_operand, second_operand)
print(result)
