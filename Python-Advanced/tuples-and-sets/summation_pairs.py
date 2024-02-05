# Summation Pairs
import time

start_time = time.time()
numbers = list(map(int, input().split()))

target = int(input())
complimentary_number_set = set()
complimentary_pairs = {}

for i in range(len(numbers)):
    complimentary_number = target - numbers[i]
    complimentary_number_set.add(complimentary_number)
    complimentary_pairs[numbers[i]] = complimentary_number

for c_number in numbers:
    if c_number in complimentary_number_set:
        complimentary_number_set.remove(complimentary_pairs[c_number])
        print(f"{c_number} + {complimentary_pairs[c_number]} = {target}")
        del complimentary_pairs[c_number]

end_time = time.time()
print(f"Time spent: {end_time - start_time}")
