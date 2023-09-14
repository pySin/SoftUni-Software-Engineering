# Number = sum of the rest of the numbers
import sys

number_of_numbers = int(input())

max_number = -sys.maxsize
sum_of_numbers = 0

for _ in range(number_of_numbers):
    current_number = int(input())
    sum_of_numbers += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == sum_of_numbers / 2:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    remainder = abs((sum_of_numbers - max_number) - max_number)
    print("No")
    print(f"Diff = {remainder}")

