# Train two steps in list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for step_2 in range(0, len(numbers), 3):
    if step_2 + 2 > len(numbers):
        print("End of list!")
        break

    inner_numbers = [numbers[step_2], numbers[step_2 + 1], numbers[step_2 + 2]]
    print(inner_numbers)
