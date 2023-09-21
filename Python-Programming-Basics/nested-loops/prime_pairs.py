# Prime Pairs
from math import ceil

# ⦁	На първия ред – началната стойност на първите първата двойка числа – цяло положително число в диапазона [10… 90]
# ⦁	На втория ред – началната стойност на втората двойка числа – цяло положително число в диапазона [10… 90]
# ⦁	На третия ред – разликата между началната и крайната стойност на  първата двойка числа – цяло положително число в диапазона [1… 9]
# ⦁	На четвъртия ред – разликата между началната и крайната стойност на  втората двойка числа – цяло положително число в диапазона [1… 9]

initial_value_first_pair = int(input())
initial_value_second_pair = int(input())
increase_value_first_pair = int(input())
increase_value_second_pair = int(input())

for i in range(initial_value_first_pair, initial_value_first_pair + increase_value_first_pair + 1):
    is_i_prime = True
    #  for i_divisor in range(2, ceil((initial_value_first_pair + increase_value_first_pair) / 2)):
    for i_divisor in range(2, i):
        # print(i_divisor)
        if i % i_divisor == 0:
            is_i_prime = False
            break
    if is_i_prime:
        # print(f"Prime {i}")

        for j in range(initial_value_second_pair, initial_value_second_pair + increase_value_second_pair + 1):
            is_j_prime = True
            for j_divisor in range(2, j):
                if j % j_divisor == 0:
                    is_j_prime = False
                    break
            if is_j_prime:
                print(f"{i}{j}")
