# Operate

#
# def operate(operator, *args):
#
#     def add():
#         return sum(args)
#
#     def subtract():
#         result = args[0]
#         for el in args[1:]:
#             result -= el
#         return result
#
#     def multiply():
#         result = 1
#         for el in args:
#             result *= el
#         return result
#
#     def divide():
#         result = args[0]
#         for el in args[1:]:
#             result /= el
#         return result
#
#     if operator == "+":
#         return add()
#     elif operator == "-":
#         return subtract()
#     elif operator == "*":
#         return multiply()
#     elif operator == "/":
#         return divide()
#
#
# print(operate("+", 1, 2, 3))
# print(operate("-", 3, 4, 5))
# print(operate("/", 2, 4, 1, 5, 3, 8))


    # operators = {
    #     "+": lambda x, y: x + y,
    #     "-": lambda x, y: x - y,
    #     "*": lambda x, y: x * y,
    #     "/": lambda x, y: x / y
    # }
    #
    # result = args[0]
    # for num in args[1:]:
    #     result = operators[operator](result, num)
    # return result


# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)
    # result = None
    # if operator == "+":
    #     result = reduce(lambda x, y: x + y, args)
    # elif operator == "-":
    #     result = reduce(lambda x, y: x - y, args)
    # elif operator == "*":
    #     result = reduce(lambda x, y: x * y, args)
    # elif operator == "/":
    #     result = reduce(lambda x, y: x / y, args)
    # return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
