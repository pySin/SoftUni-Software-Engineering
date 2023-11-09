# Factorial Division

def factorial(num1, num2):
    value_holder1 = 1
    for multiplier in range(1, num1 + 1):
        value_holder1 *= multiplier

    value_holder2 = 1
    for multiplier in range(1, num2 + 1):
        value_holder2 *= multiplier

    return f"{value_holder1 / value_holder2:.2f}"


integer_1 = int(input())
integer_2 = int(input())
print(factorial(integer_1, integer_2))
