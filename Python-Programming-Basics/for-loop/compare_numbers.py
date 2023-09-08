# Compare numbers

number_of_number_pairs = int(input())
left_number = 0
right_number = 0

number_of_number_pairs *= 2
# print(number_of_number_pairs / 2)

for i in range(1, number_of_number_pairs + 1):
    # print(i)
    current_number = int(input())
    if i <= number_of_number_pairs / 2:
        left_number += current_number
    elif i > number_of_number_pairs / 2:
        # print("Current number: ", current_number)
        right_number += current_number

# print("Left Number: ", left_number)
# print("Right Number: ", right_number)

if left_number == right_number:
    print(f"Yes, sum = {left_number}")
elif left_number != right_number:
    print(f"No, diff = {abs(left_number - right_number)}")
