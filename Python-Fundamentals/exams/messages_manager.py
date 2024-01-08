# Messages Manager


def add(messages: dict, instructions: list) -> dict:
    username = instructions[1]
    sent = int(instructions[2])
    received = int(instructions[3])
    if username in messages:
        pass
    else:
        messages[username] = [sent, received]
    return messages


def send_message(messages: dict, instructions: list, possible_messages: int) -> dict:
    sender = instructions[1]
    receiver = instructions[2]

    if sender in messages and receiver in messages:
        messages[sender][0] += 1
        messages[receiver][1] += 1
        if sum(messages[sender]) == possible_messages:
            print(f"{sender} reached the capacity!")
            messages.pop(sender)

        if sum(messages[receiver]) == possible_messages:
            print(f"{receiver} reached the capacity!")
            messages.pop(receiver)
    return messages


def empty(messages: dict, instructions: list):
    username = instructions[1]
    if username == "All":
        messages.clear()
    elif username in messages:
        messages.pop(username)
    return messages


def display_data(messages: dict):
    print(f"Users count: {len(messages)}")
    for user in messages:
        print(f"{user} - {sum(messages[user])}")


def call_functions():
    messages = {}
    possible_messages = int(input())

    command = input()

    while command != "Statistics":
        instructions = command.split("=")
        action = instructions[0]

        if action == "Add":
            messages = add(messages, instructions)
        elif action == "Message":
            messages = send_message(messages, instructions, possible_messages)
        elif action == "Empty":
            messages = empty(messages, instructions)

        command = input()

    display_data(messages)


if __name__ == "__main__":
    call_functions()
