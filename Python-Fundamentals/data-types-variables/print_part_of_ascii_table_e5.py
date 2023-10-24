# Print part of ascii table

start_of_ASCII_range = int(input())
end_of_ASCII_range = int(input())

ascii_chars = []

for ascii_number in range(start_of_ASCII_range, end_of_ASCII_range + 1):
    ascii_chars.append(chr(ascii_number))

for i in ascii_chars:
    print(i, end=" ")
