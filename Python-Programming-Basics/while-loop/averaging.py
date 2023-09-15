# Averaging

number_of_numbers = int(input())
numbers_sum = 0


for i in range(number_of_numbers):
    current_number = int(input())

    numbers_sum += current_number

print(f"{numbers_sum / number_of_numbers:.2f}")
