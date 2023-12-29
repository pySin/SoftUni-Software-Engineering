# Activation Keys


def contains(activation_key: str, instructions: list):
    substring = instructions[1]
    if substring in activation_key:
        print(f"{activation_key} contains {substring}")
    else:
        print("Substring not found!")


def flip(activation_key: str, instructions: list):
    case = instructions[1]
    first_index = int(instructions[2])
    last_index = int(instructions[3])

    if case == "Upper":
        activation_key = f"{activation_key[:first_index]}" \
                         f"{activation_key[first_index:last_index].upper()}{activation_key[last_index:]}"
    elif case == "Lower":
        activation_key = f"{activation_key[:first_index]}" \
                         f"{activation_key[first_index:last_index].lower()}{activation_key[last_index:]}"
    print(activation_key)
    return activation_key


def slicing(activation_key: str, instructions: list):
    start_index = int(instructions[1])
    end_index = int(instructions[2])
    activation_key = f"{activation_key[:start_index]}{activation_key[end_index:]}"
    print(activation_key)
    return activation_key


def call_functions():
    activation_key = input()

    command = input()

    while command != "Generate":

        instructions = command.split(">>>")
        action = instructions[0]

        if action == "Contains":
            contains(activation_key, instructions)
        elif action == "Flip":
            activation_key = flip(activation_key, instructions)
        elif action == "Slice":
            activation_key = slicing(activation_key, instructions)

        command = input()
    print(f"Your activation key is: {activation_key}")


if __name__ == "__main__":
    call_functions()
