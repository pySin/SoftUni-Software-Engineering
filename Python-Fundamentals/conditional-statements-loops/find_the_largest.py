# Find the largest


base_number = int(input())

base_number_str = str(base_number)
biggest_number = ""

while True:
    is_largest_single_digit = False
    for i in range(len(base_number_str)):
        checked_numbers = 0
        for j in range(len(base_number_str)):
            if i == j:
                continue
            if int(base_number_str[i]) >= int(base_number_str[j]):
                checked_numbers += 1
                if checked_numbers == len(base_number_str) - 1:
                    biggest_number += base_number_str[i]
                    base_number_str = base_number_str[:i] + base_number_str[i + 1:]
                    is_largest_single_digit = True
                    break
        if is_largest_single_digit:
            break

    if len(base_number_str) == 1:
        biggest_number += base_number_str
        break

print(biggest_number)
