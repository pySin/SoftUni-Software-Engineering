# Tests


# print("Test")

# --

# def sum_nums(a, b, c):
#     return a + b + c
#
#
# result = sum_nums(5, 5, 4)
#
# print(result)

## def sum_func(*args, **kwargs): ##


# *args
# def sum_nums(a, b, *args):
#     return a, b, args
#
#
# result = type(sum_nums(5, 6))
# print(sum_nums(5, 8))
# print(result)
# # print(sum_nums())  # Using arg with 0 arguments
#
# print(sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))

# == **kwargs - Packing Argument Into dictionary

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{value}, {key}")
#
#
# greet_me(Peter="Hello", George="Bye")

# - *args, **kwargs

# def diff_arguments(a, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
#
#
# diff_arguments(1)
# diff_arguments(1, 4, 6, 7, season="Autumn", day="Tuesday")
# diff_arguments(1, season="Autumn", day="Tuesday")  # Omitting the *args
# diff_arguments(1, 4, 6, 7)  # Omitting the **kwargs

# -- Packing and unpacking

# - Unpacking *args
# def print_nums(a, b, c):
#     print(a, b, c)
#
#
# nums = [1, 2, 3]
# print_nums(*nums)

# Unpacking **kwargs in functions

# def sum_func(name, age):
#     print(f"{name} is {age} years old")
#
#
# person = {"age": 20, "name": "Peter"}  # The names must match the function parameters.
# sum_func(**person)                     # The parameter sequence is not important.

# -- sorted(iterable, key=None, reverse=false) function

# a = [10, -2, 4, 3]
# print(a)
# print(sorted(a, reverse=True))
# print(a)

# - sorted with dictionary

# my_dict = {"Peter": 21, "George": 18, "John": 45}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
# print(sorted_dict)


# -- List Comprehension give to function

# def sum_nums(*args):
#     print(*args)
#
#
# sum_nums(*[el for el in range(10)])

# --- Nested Functions

# def some_func():
#     def some_func_2():
#         return 5
#
#     print(some_func_2())
#     return 6
#
#
# some_func()

# -- Example

# def factorial(number):
#     if not isinstance(number, int) or number < 0:
#         return f"Sorry 'number' is incorrect."
#
#     def inner_factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact = fact * i
#         return fact
#     return inner_factorial(number)
#
#
# print(factorial(6))

# - Return function inside another functions

# def calculator(operator):
#
#     def addition(a, b):
#         return a + b
#
#     def subtraction(a, b):
#         return a - b
#
#     if operator == "+":
#         return addition  # Return a REFERENCE to a function
#     elif operator == "-":
#         return subtraction
#
#
# operation = calculator("-")  # operation variable holds the whole inner function "subtraction"
# print(operation)
# print(type(operation))
# print(operation(4, 5))

# - Lexical Closures - inner function captures infor from outer function

# def outside_function(number):
#     def inside_function():
#         return number
#     return inside_function
#
#
# print(outside_function(10)())


# --- Recursion

# def sum_nums():
#     print("invoking")
#     sum_nums()
#
#
# sum_nums()

# --

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))

# -- args, kwargs


# def ar_kwa_check(var, *args, **kwargs):
#     print(var)
#     print(args)
#     print(kwargs)
#
#
# my_args = [1, 2, 3]
# my_dict = {"four": 4, "five": 5}
#
# ar_kwa_check(*my_args, **my_dict)

# Function Reference in a tuple


# def sum_nums(a, b):
#     return a + b
#
#
# def div_nums(a, b):
#     return a - b
#
#
# functions_tuple = (sum_nums, div_nums)
# functions_list = [sum_nums, div_nums]
# print(functions_tuple[0](2, 3))
# print(functions_list[0](2, 3))

# --

# ls = [1, 2, 3]
# ls_2 = [1, 2, ls]
# print(ls_2)

# -- Recursion test

# def recur_test(num):
#     num -= 1
#     if num == 1:
#         return num
#     return 1 + recur_test(num)
#
#
# print(recur_test(5))

# --

# a = 15.089999999999998
# print(round(a, 1))

# --

# def a_kw(*args, **kwargs):
#     for key, value in kwargs.items():
#         print(f"Key: {key}, Value: {value}")
#     return args, kwargs
#
#
# aw, k_w = a_kw("x", 18, "b", var_1=11, var_2="GOOG")
# dicti = {"z": 66, "s": 77}
# a_kw(4, 5, **dicti)  # Have to unpack the dictionary

# -- advanced sorting

# list_1 = ["Toyota", "Mercedes", "Lamborghini", "Ferrari", "Carambolonni"]
#
# list_sorted = sorted(list_1, key=lambda x: (ord(x[-1]), -len(x)))
# print(list_sorted)

# -- Nested Functions

# def outer_func(num_1):
#
#     def inner_func(num_2):
#         print(f"Outer: {num_1}, Inner: {num_2}")
#
#     return inner_func
#
#
# outer = outer_func(4)
# print(outer(5))

# -- Recursion

# def rec_func(n):
#     if n == 1:
#         return n
#     print(n)
#     rec_func(n - 1)
#
#
# rec_func(12)

# -- reduce

from functools import reduce

log_words = ["someletters", "overthere", "perturbators", "alhambrenos"]


# def elongate(a, b):
#     if len(a) > 5:
#         new = a[0] + b[0]
#     else:
#         new = a + b[0]
#     return new
#
#
# reduced_e_long = reduce(elongate, log_words)
# print(reduced_e_long)

# -- dictionary with function references

# def sum_it(n1, n2):
#     return n1 + n2
#
#
# def div(n1, n2):
#     return n1 / n2


# def operations(operation):
#     math_ops = {
#         "sum_nums": sum_it,
#         "divide": div
#     }
#     return math_ops[operation]
#
#
# print(operations("sum_nums")(3, 4))

# --

# list_1 = [1, "two", "three", True]
#
# ternary = "Is Tuple" if isinstance(list_1, tuple) else "Not a Tuple"
# print(ternary)

# -- Function References in a tuple

# def sum_it(n1, n2):
#     return n1 + n2
#
#
# def div(n1, n2):
#     return n1 / n2
#
#
# functions_collection = (sum_it, div)
# values = (3, 4)
#
# for operation in functions_collection:
#     print(f"Function : {operation.__name__} Result: {operation(*values)}")


# __name__ method for functions

# def sum_it(n1, n2):
#     return n1 + n2
#
#
# def div(n1, n2):
#     return n1 / n2
#
#
# functions_collection = (sum_it, div)
# for function in functions_collection:
#     print(f"{function.__name__} - {function(2, 5)}")


# def function_1():
#     return 9
#
#
# print(function_1.__name__)

# Build File Path

# import os
#
#
# current_directory = os.getcwd()
# directory_path = "test_dir"
# file_name = "make_file_test.txt"
# # full_path = os.path.join(current_directory, directory_path, file_name)
# full_path = os.path.join(current_directory, file_name)
# print(full_path)

# with open(full_path, "a") as f:
#     f.write("test 32.01.2024")

# --

# import os
#
# current_directory = os.getcwd()
# directory_path = "test_dir"
# file_name = "make_file_test.txt"
# full_path = os.path.join(current_directory, directory_path, file_name)
#
# with open(full_path) as f:
#     for i in range(3):
#         red = f.read(2)
#         print(red)

# -- readline

# import os
#
# current_directory = os.getcwd()
# directory_path = "test_dir"
# file_name = "make_file_test.txt"
# full_path = os.path.join(current_directory, directory_path, file_name)
#
# with open(full_path) as f:
#     for line in f:
#         print(line, end="")


# writelies

# import os
#
# current_directory = os.getcwd()
# directory_path = "test_dir"
# file_name = "make_file_test.txt"
# full_path = os.path.join(current_directory, directory_path, file_name)

# lines = ["line 1", "line_2", "line 3"]
# with open(full_path, "a") as f:
#     f.writelines(lines)  # Can't have new lines with "writelines"

# -- Delete a file - os.remove(full_path)

# import os
#
# current_directory = os.getcwd()
# directory_path = "test_dir"
# file_name = "second_text_file.txt"
# full_path = os.path.join(current_directory, directory_path, file_name)
#
# os.remove(full_path)


# Open 2 files in the same row

# import os
#
# current_directory = os.getcwd()
# directory_path = "test_dir"
# file_name = "second_text_file.txt"
# file_name_2 = "make_file_test.txt"
# full_path = os.path.join(current_directory, directory_path, file_name)
# full_path_2 = os.path.join(current_directory, directory_path, file_name_2)
#
# with open(full_path) as f1, open(full_path_2) as f2:
#     read_first = f1.read()
#     read_second = f2.read()
#     print("FIRST " + read_first, end="")
#     print("SECOND " + read_second, end="")

# os.walk()

# import os
#
# for base, dirs, filenames in os.walk(os.getcwd()):
#     print("BASE: ", base)
#     print("DIRS: ", dirs)
#     print("FILENAMES: ", filenames)

# packing train

# values = [1, 2, 3, 4, 5]
# first, *other = values
# print(first)
# print(*other)


