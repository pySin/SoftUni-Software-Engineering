# Smallest and biggest Numbers
import sys

number_of_numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(1, number_of_numbers + 1, 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print("Max number: " + str(max_number))
print("Min number: " + str(min_number))

