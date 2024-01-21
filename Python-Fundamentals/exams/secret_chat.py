# Secret Chat


def insert_space(concealed_message: str, instructions: list) -> str:
    index = int(instructions[1])
    concealed_message = f"{concealed_message[:index]} {concealed_message[index:]}"
    print(concealed_message)
    return concealed_message


def reverse(concealed_message: str, instructions: list) -> str:
    substring = instructions[1]
    if substring in concealed_message:
        reversed_string = substring[::-1]
        concealed_message = concealed_message.replace(substring, "", 1) + reversed_string
        print(concealed_message)
    else:
        print("error")
    return concealed_message


def change_all(concealed_message: str, instructions: list) -> str:
    substring = instructions[1]
    replacement = instructions[2]
    concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)
    return concealed_message


def call_functions():
    concealed_message = input()

    # Functions Mapper
    message_data = {
        "message": concealed_message,
        "InsertSpace": insert_space,
        "Reverse": reverse,
        "ChangeAll": change_all
    }

    command = input()

    while command != "Reveal":

        instructions = command.split(":|:")
        action = instructions[0]
        message_data["message"] = message_data[action](message_data["message"], instructions)

        command = input()
    print(f"You have a new text message: {message_data['message']}")


if __name__ == "__main__":
    call_functions()
