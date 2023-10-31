# Moving Targets


target_sequence = [int(x) for x in input().split()]


command = input()

while command != "End":

    instructions = command.split()

    if instructions[0] == "Shoot":
        shoot_index = int(instructions[1])
        shoot_power = int(instructions[2])
        if shoot_index in range(len(target_sequence)):
            target_sequence[shoot_index] -= shoot_power
        else:
            command = input()
            continue
        if target_sequence[shoot_index] < 1:
            target_sequence.pop(shoot_index)

    elif instructions[0] == "Add":
        add_index = int(instructions[1])
        add_value = int(instructions[2])
        if add_index in range(len(target_sequence)):
            target_sequence.insert(add_index, add_value)
        else:
            print("Invalid placement!")

    elif instructions[0] == "Strike":
        strike_index = int(instructions[1])
        strike_radius = int(instructions[2])
        lower_index = strike_index - strike_radius
        upper_index = strike_index + strike_radius
        if lower_index < 0 or upper_index > len(target_sequence):
            print("Strike missed!")
        else:
            for _ in range((strike_radius * 2) + 1):
                target_sequence.pop(lower_index)
    command = input()

target_sequence = [str(x) for x in target_sequence]
print("|".join(target_sequence))
