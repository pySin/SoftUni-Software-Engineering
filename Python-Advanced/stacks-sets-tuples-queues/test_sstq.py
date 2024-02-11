# Test SSTQ


# a = "-1"
#
# if a.isdigit():
#     print(a)

# -- Function as a value of a dictionary

# def outer_function(num_1, num_2):
#     return num_1 - num_2
#
#
# my_dict = {
#     "a": lambda a, b: a + b,
#     "b": outer_function
# }
#
# print(my_dict["a"](7, 14))
# print(my_dict["b"](11, 12))

# from collections import deque
#
# milk_portions = deque([])
#
# print("Milk: ", end="")
# print(*milk_portions, sep=", ")

# comprehension in join()

# from collections import deque
#
# sequence = deque([1, 2, 3, 4])
#
# print(f"Sequence {', '.join([str(x) for x in sequence]) if len(sequence) > 6 else ', '.join([str(x) + 'zz' for x in sequence])}")

x = 5

d_list = [x for x in range(x)] if x > 6 else [x + 20 for x in range(x)]

[print(x) for x in d_list]

