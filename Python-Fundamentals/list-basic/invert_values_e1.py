# Invert values

string_of_numbers = input().split()
opposite_nums = []

for element in string_of_numbers:
    current_number = -int(element)
    opposite_nums.append(current_number)

print(opposite_nums)
