# Test

# print("Test Successful")

# def sum_numbers(a: int, b: int):
#     return a + b
#
#
# for _ in range(3):
#     a = int(input("Enter a value for A:"))
#     b = int(input("Enter a value for B:"))
#     result = sum_numbers(a, b)
#     print(result)

# def even_numbers(number):
#     return number % 2 == 0
#
#
# list_1 = [1, 2, 3, 4, 5, 6]
# even = list(filter(even_numbers, list_1))
# print(even)

# MAP

# numbers = list(map(int, input().split(", ")))
# print(numbers)
# print(type(numbers[0]))
# print(sorted(numbers, reverse=True))

# print(dir("__builtins__"))

# def hello(first_name, last_name, town):
#     return f"Hello {first_name} {last_name} from {town}"


# def get_user_data():
#     user_first_name = input()
#     user_second_name = input()
#     user_town = input()
#     return hello(user_first_name, user_second_name, user_town)
#
#
# sentence = get_user_data()
# print(sentence)

# names = ["Ismail", "Bruno", "Nuno", "Barakaguira"]
#
# sorted_names = sorted(names, key=len, reverse=True)
# print(sorted_names)

# def my_function(digit):
#     digit += 1
#
#
# print(my_function(3))

# -- Multiple returns

# def divide_it(number_1, number_2):
#     if number_2 == 0:
#         return "Error. Can\'t divide by zero"
#     else:
#         if number_1 / number_2 < 1:
#             return "Number smaller than 1."
#         else:
#             return "number greater than 1"


# first_number = int(input())
# second_number = int(input())
# print(divide_it(first_number, second_number))

# def greet(name, surname="Mehmedov", greeting="Hello"):
#     return f"{greeting} {name} {surname}"
#
#
# greeting_phrase = greet("Sinan", "Kalufov")
# print(greeting_phrase)

# def summing(a, b):
#     return a + b
#
#
# get_sum = summing(b=12, a=66)
# print(get_sum)

# --
# import math
#
#
# def length():
#     x1 = float(input())
#     y1 = float(input())
#     x2 = float(input())
#     y2 = float(input())
#
#     closest_point = None
#
#     if abs(x1) * abs(y1) <= abs(x2) * abs(y2):
#         closest_point = ((math.floor(x1), math.floor(y1)), (math.floor(x2), math.floor(y2)))
#     elif abs(x2) * abs(y2) < abs(x1) * abs(y1):
#         closest_point = ((math.floor(x2), math.floor(y2)), (math.floor(x1), math.floor(y1)))
#
#     results = ""
#     for point in closest_point:
#         results += str(point)
#     return results


# if __name__ == "__main__":
#     result_1 = length()
#     result_2 = length()
#     print(result_1)


#---------
# from math import floor, sqrt
# def whats_closer(arg1, arg2, arg3, arg4):
#     one = arg1 + arg2
#     two = arg3 + arg4
#     if one > two:
#         if abs(x1) + abs(x2) > abs(y1) + abs(y2):
#             return f"({y1}, {y2})({x1}, {x2})"
#         else:
#             return f"({x1}, {x2})({y1}, {y2})"
#     elif one < two:
#         if abs(z1) + abs(z2) > abs(v1) + abs(v2):
#             return f"({v1}, {v2})({z1}, {z2})"
#         else:
#             return f"({z1}, {z2})({v1}, {v2})"
#     else:
#         if abs(z1) + abs(z2) > abs(v1) + abs(v2):
#             return f"({v1}, {v2})({z1}, {z2})"
#         else:
#             return f"({z1}, {z2})({v1}, {v2})"
#
#
# x1, x2, y1, y2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(
#     float(input()))
# z1, z2, v1, v2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(
#     float(input()))
#
# sum_x = floor(abs(x1) + abs(x2))
# sum_y = floor(abs(y1) + abs(y2))
# sum_z = floor(abs(z1) + abs(z2))
# sum_v = floor(abs(v1) + abs(v2))
# print(whats_closer(sum_x, sum_y, sum_z, sum_v))

# -------------------
