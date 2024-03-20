# Calculate Logarithm
from math import log


def call_functions():
    number = int(input())
    logarithm_base = input()
    if logarithm_base.isdigit():
        print(f"{log(number, int(logarithm_base)):.2f}")
    elif logarithm_base == "natural":
        print(f"{log(number):.2f}")


if __name__ == "__main__":
    call_functions()
