# Odd Even Position
import sys


numbers_count = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, numbers_count + 1):
    current_num = float(input())

    if i % 2 == 0:
        even_sum += current_num
        if current_num > even_max:
            even_max = current_num

        if current_num < even_min:
            even_min = current_num

    if i % 2 != 0:
        odd_sum += current_num
        if current_num > odd_max:
            odd_max = current_num

        if current_num < odd_min:
            odd_min = current_num


print(f"OddSum={odd_sum :.2f},")
if odd_min == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min :.2f},")
if odd_max == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max :.2f},")

print(f"EvenSum={even_sum :.2f},")

if even_min == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min :.2f},")

if even_max == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max :.2f}")
