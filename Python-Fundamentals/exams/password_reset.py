# Password Reset


def take_odd(password):
    password = "".join([password[i] for i in range(len(password)) if i % 2 != 0])
    print(password)
    return password


def cut(password, instructions):
    index = int(instructions[1])
    length = int(instructions[2])
    password = password.replace(password[index: index + length], "", 1)
    return password


def substitute_section(password, instructions):
    substring = instructions[1]
    substitute = instructions[2]
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")
    return password


def call_functions():
    password = input()

    command = input()

    while command != "Done":
        instructions = command.split()
        action = instructions[0]
        if action == "TakeOdd":
            password = take_odd(password)
        elif action == "Cut":
            password = cut(password, instructions)
            print(password)
        elif action == "Substitute":
            password = substitute_section(password, instructions)

        command = input()
    print(f"Your password is: {password}")


if __name__ == "__main__":
    call_functions()
