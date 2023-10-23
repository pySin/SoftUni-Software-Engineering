import decimal
from decimal import Decimal
#
# a = 0.1
# b = 0.1
# c = 0.1
#
# print("Normal Accuracy", a + b + c)
#
# e = Decimal("0.1")
# f = Decimal("0.1")
# j = Decimal("0.1")
#
# print("Decimal Accuracy", e + f + j)
# print(type(e))
# print(isinstance(e, decimal.Decimal))


# def process_variable(var):
#     if isinstance(var, int):
#         print("Processing an integer", var)
#     elif isinstance(var, str):
#         print("Processing an string", var)
#     if isinstance(var, list):
#         print("Processing an list", var)
#     if isinstance(var, tuple):
#         print("Processing an tuple", var)
#     else:
#         print("Unknown type!")
#
#
# process_variable(34)
# process_variable("Buy")
# process_variable([1, 2, 3])
# process_variable((4, 5, 6))
# process_variable(3.14)


# name = "Dani"
#
# print(name[3])
# name[2] = p # Error

# phrase = "Hello SoftUni"
# new_phrase = phrase.replace("Hello", "Hi")
#
# print(new_phrase)


numbers = [3, 5, 3, 1, 2, 2, 1, "one", "three", 2, 3, 4, 5]
set_num = set(numbers)
print(set_num)
print(list(set_num))
