# Compare sums between even and odd numbers

first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):

    even_numbers_sum = 0
    odd_numbers_sum = 0

    for digit in range(1, len(str(number)) + 1):
        if digit % 2 == 0:
            even_numbers_sum += int(str(number)[digit - 1])
        else:
            odd_numbers_sum += int(str(number)[digit - 1])

    if even_numbers_sum == odd_numbers_sum:
        print(number, end=" ")
