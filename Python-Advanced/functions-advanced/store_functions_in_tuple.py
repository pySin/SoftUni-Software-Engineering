# Store functions in a tuple

def func_1(a, b):
    return a + b


def func_2(a, b):
    return a * b


funcs_tuple = (func_1, func_2)

for function in funcs_tuple:
    print(function(5, 6))