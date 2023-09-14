# Input and sum

number_of_numbers = int(input())
sum_of_numbers = 0

for i in range(1, number_of_numbers + 1, 1):
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)
