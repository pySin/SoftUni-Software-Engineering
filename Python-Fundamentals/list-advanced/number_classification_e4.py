# Number Classification

row_of_numbers = input().split(", ")
row_of_numbers = list(map(int, row_of_numbers))

positive_numbers = [number for number in row_of_numbers if number >= 0]
negative_numbers = [number for number in row_of_numbers if number < 0]
even_numbers = [number for number in row_of_numbers if number % 2 == 0]
odd_numbers = [number for number in row_of_numbers if number % 2 != 0]

print(f"Positive: {', '.join(map(str, positive_numbers))}")
print(f"Negative: {', '.join(map(str, negative_numbers))}")
print(f"Even: {', '.join(map(str, even_numbers))}")
print(f"Odd: {', '.join(map(str, odd_numbers))}")
