# numbers filter

# numbers_count = int(input())
#
# all_numbers = []
#
# for _ in range(numbers_count):
#     current_number = int(input())
#     all_numbers.append(current_number)
#
# command = input()
# resulting_list = []

# if command == "even":
#     for i in range(len(all_numbers)):
#         if all_numbers[i] % 2 == 0:
#             resulting_list.append(all_numbers[i])
# elif command == "odd":
#     for i in range(len(all_numbers)):
#         if all_numbers[i] % 2 != 0:
#             resulting_list.append(all_numbers[i])
# elif command == "negative":
#     for i in range(len(all_numbers)):
#         if all_numbers[i] < 0:
#             resulting_list.append(all_numbers[i])
# elif command == "positive":
#     for i in range(len(all_numbers)):
#         if all_numbers[i] >= 0:
#             resulting_list.append(all_numbers[i])
#
# print(resulting_list)

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

numbers_count = int(input())

all_numbers = []

for _ in range(numbers_count):
    current_number = int(input())
    all_numbers.append(current_number)

command = input()
resulting_list = []

for num in all_numbers:

    filter_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_NEGATIVE and num < 0) or
        (command == COMMAND_POSITIVE and num >= 0)
    )

    if filter_command:
        resulting_list.append(num)

print(resulting_list)
