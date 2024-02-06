# -- Function as a value of a dictionary

def outer_function(num_1, num_2):
    return num_1 - num_2


my_dict = {
    "a": lambda a, b: a + b,
    "b": outer_function
}

print(my_dict["a"](7, 14))
print(my_dict["b"](11, 12))
