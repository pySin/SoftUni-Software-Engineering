# Numbers Bigger than average


numbers_sequence = [int(x) for x in input().split()]

average = sum(numbers_sequence) / len(numbers_sequence)
bigger_than_average = []

for number in numbers_sequence:
    if number > average:
        bigger_than_average.append(number)

if bigger_than_average:
    reversed_numbers = sorted(bigger_than_average, reverse=True)
    if len(reversed_numbers) > 5:
        reversed_numbers = reversed_numbers[:5]
    numbers_print = ""
    for number in reversed_numbers:
        numbers_print += str(number) + " "
    print(numbers_print[:-1])
else:
    print("No")
