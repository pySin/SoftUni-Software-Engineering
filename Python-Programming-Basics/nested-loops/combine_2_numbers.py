# Combine 2 numbers

first_number = int(input())
second_number = int(input())
magic_number = int(input())
combinations = 0

is_found = False
for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        combinations += 1
        if i + j == magic_number:
            print(f"Combinations N: {combinations} ({i} + {j}) = {magic_number}")
            is_found = True
            break
    if is_found:
        break
