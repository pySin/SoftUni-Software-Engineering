# Array Modifier


initial_array_values = [int(x) for x in input().split()]

command = input()

while command != "end":

    instructions = command.split()

    if instructions[0] == "swap":
        first_value = initial_array_values[int(instructions[1])]
        second_value = initial_array_values[int(instructions[2])]
        initial_array_values[int(instructions[1])] = second_value
        initial_array_values[int(instructions[2])] = first_value
    elif instructions[0] == "multiply":
        first_index = int(instructions[1])
        second_index = int(instructions[2])

        multiplication = initial_array_values[first_index] * initial_array_values[second_index]
        initial_array_values[first_index] = multiplication
    elif instructions[0] == "decrease":
        for i in range(len(initial_array_values)):
            initial_array_values[i] = initial_array_values[i] - 1

    command = input()

print(str(initial_array_values)[1:-1])
