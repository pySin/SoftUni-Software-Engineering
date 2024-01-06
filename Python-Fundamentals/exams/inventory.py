# Inventory


collecting_items = input().split(", ")

command = input()

while command != "Craft!":

    instructions = command.split(" - ")
    action = instructions[0]

    if action == "Collect":
        if instructions[1] not in collecting_items:
            collecting_items.append(instructions[1])
    elif action == "Drop":
        if instructions[1] in collecting_items:
            collecting_items.remove((instructions[1]))

    elif action == "Combine Items":
        old_item = instructions[1].split(":")[0]
        new_item = instructions[1].split(":")[1]
        if old_item in collecting_items:
            collecting_items.insert(collecting_items.index(old_item) + 1, new_item)
    elif action == "Renew":
        if instructions[1] in collecting_items:
            collecting_items.append(collecting_items.pop(collecting_items.index(instructions[1])))

    command = input()

print(", ".join(collecting_items))

