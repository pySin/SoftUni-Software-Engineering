# Sort a list by an inner list value.
# Sort a dictionary by value


# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x2 = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# trans_tuple = sorted(x.items(), key=lambda item: item[1])
# print(trans_tuple)

# print(x.items())

groups_of_numbers = ([2, 4, 23], [20, 22, 21], [33, 75, 6], [25, 6, 11], [2, 44, 12])
# sorted_by_third = sorted(groups_of_numbers, key=lambda x: x[2])
# print(sorted_by_third)

ordering_factor = []
for numbers in groups_of_numbers:
    ordering_factor.append(numbers[1])

ordering_factor = sorted(ordering_factor)

new_order = []

for order_number in ordering_factor:
    for number_group in groups_of_numbers:
        if number_group[1] == order_number:
            new_order.append(number_group)

print(new_order)
