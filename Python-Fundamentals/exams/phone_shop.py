# Phone Shop


phones = input().split(", ")

command = input()

while command != "End":

    instructions = command.split(" - ")
    action = instructions[0]

    if action == "Add":
        phone = instructions[1]
        if phone in phones:
            command = input()
            continue
        else:
            phones.append(phone)

    elif action == "Remove":
        phone = instructions[1]
        if phone not in phones:
            command = input()
            continue
        else:
            phones.remove(phone)

    elif action == "Bonus phone":
        old_phone = instructions[1].split(":")[0]
        new_phone = instructions[1].split(":")[1]
        if old_phone not in phones:
            command = input()
            continue
        else:
            old_phone_index = phones.index(old_phone)
            phones.insert(old_phone_index + 1, new_phone)

    elif action == "Last":
        phone = instructions[1]
        if phone not in phones:
            command = input()
            continue
        else:
            phone_index = phones.index(phone)
            phones.append(phones.pop(phone_index))

    command = input()

print(", ".join(phones))
