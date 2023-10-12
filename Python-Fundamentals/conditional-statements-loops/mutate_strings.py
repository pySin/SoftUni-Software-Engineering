# Mutate Strings

first_string = input()
second_string = input()

# carrier_string = ""
#
# for i in range(len(first_string)):
#     if first_string[i] == second_string[i]:
#         carrier_string += first_string[i]
#         continue
#     else:
#         carrier_string += second_string[i]
#         print(carrier_string, end="")
#         for j in range(i + 1, len(first_string)):
#             print(first_string[j], end="")
#         print()

for i in range(len(first_string)):
    if first_string[i] == second_string[i]:
        continue
    else:
        print(second_string[:i + 1] + first_string[i + 1:])
