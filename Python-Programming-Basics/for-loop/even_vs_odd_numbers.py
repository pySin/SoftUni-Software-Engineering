# Even VS Odd

number_of_numbers = int(input())
even_numbers = 0
odd_numbers = 0

for i in range(0, number_of_numbers):
    current_number = int(input())
    if i % 2 == 0:
        even_numbers += current_number
    elif i % 2 != 0:
        odd_numbers += current_number

if even_numbers == odd_numbers:
    print(f"Yes")
    print(f"Sum = {even_numbers}")
else:
    print(f"No")
    print(f"Diff = {abs(even_numbers - odd_numbers)}")
