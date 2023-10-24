# Sum of chars

number_of_ASCII_chars = int(input())

sum_of_ASCII_chars = 0

for i in range(number_of_ASCII_chars):
    current_char = input()
    sum_of_ASCII_chars += ord(current_char)

print(f"The sum equals: {sum_of_ASCII_chars}")
