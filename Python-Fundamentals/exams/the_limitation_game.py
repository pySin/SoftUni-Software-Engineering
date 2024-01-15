# The Limitation Game


def move(encrypted_message: str, instruction: list) -> str:
    moves = int(instruction[1])
    for _ in range(moves):
        encrypted_message = encrypted_message[1:] + encrypted_message[0]
    return encrypted_message


def insert(encrypted_message: str, instruction: list) -> str:
    index = int(instruction[1])
    value = instruction[2]
    encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    return encrypted_message


def change_all(encrypted_message: str, instruction: list) -> str:
    old_string = instruction[1]
    new_string = instruction[2]
    encrypted_message = encrypted_message.replace(old_string, new_string)
    return encrypted_message


def call_functions():
    encrypted_message = input()
    command = input()
    while command != "Decode":
        instruction = command.split("|")
        action = instruction[0]

        command = input()
        if action == "Move":
            encrypted_message = move(encrypted_message, instruction)
        elif action == "Insert":
            encrypted_message = insert(encrypted_message, instruction)
        elif action == "ChangeAll":
            encrypted_message = change_all(encrypted_message, instruction)
    print(f"The decrypted message is: {encrypted_message}")

    #         number_of_letters = int(instruction[1])
    #         for _ in range(number_of_letters):
    #             encrypted_message.append(encrypted_message.pop(0))
    #     elif action == "Insert":
    #         index = int(instruction[1])
    #         value = instruction[2]
    #         encrypted_message.insert(index, value)
    #     elif action == "ChangeAll":
    #         old_substring = instruction[1]
    #         new_substring = instruction[2]
    #         temporary_string = "".join(encrypted_message)
    #         temporary_string = temporary_string.replace(old_substring, new_substring)
    #         encrypted_message = list(temporary_string)
    #
    #     command = input()
    # print(f"The decrypted message is: {''.join(encrypted_message)}")


if __name__ == "__main__":
    call_functions()
