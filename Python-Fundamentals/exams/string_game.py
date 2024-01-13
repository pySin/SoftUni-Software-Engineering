# String Game


def change(string: str, instructions: list) -> str:
    char = instructions[1]
    replacement = instructions[2]
    string = string.replace(char, replacement)
    print(string)
    return string


def include(string: str, instructions: list):
    substring = instructions[1]
    if substring in string:
        print("True")
    else:
        print("False")


def end(string: str, instructions: list):
    substring = instructions[1]
    if string.endswith(substring):
        print("True")
    else:
        print("False")


def first_index(string: str, instructions: list):
    char = instructions[1]
    index = string.find(char)
    print(index)


def cut(string: str, instructions: list):
    start_string = int(instructions[1])
    count = int(instructions[2])
    string = string[start_string: start_string + count]
    print(string)


def call_functions():
    string = input()

    command = input()

    while command != "Done":
        instructions = command.split()
        action = instructions[0]

        if action == "Change":
            string = change(string, instructions)
        elif action == "Includes":
            include(string, instructions)
        elif action == "End":
            end(string, instructions)
        elif action == "Uppercase":
            string = string.upper()
            print(string)
        elif action == "FindIndex":
            first_index(string, instructions)
        elif action == "Cut":
            cut(string, instructions)
        command = input()


if __name__ == "__main__":
    call_functions()
