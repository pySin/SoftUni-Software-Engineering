# Shopping List


shopping_list = input().split("!")

command = input()

while command != "Go Shopping!":

    instructions = command.split()

    if instructions[0] == "Urgent":
        if instructions[1] in shopping_list:
            command = input()
            continue
        else:
            shopping_list.insert(0, instructions[1])

    if instructions[0] == "Unnecessary":
        if instructions[1] in shopping_list:
            shopping_list.remove(instructions[1])
        else:
            command = input()
            continue

    if instructions[0] == "Correct":
        if instructions[1] in shopping_list:
            shopping_list[shopping_list.index(instructions[1])] = instructions[2]
        else:
            command = input()
            continue
    if instructions[0] == "Rearrange":
        if instructions[1] in shopping_list:
            shopping_list.append(shopping_list.pop(shopping_list.index(instructions[1])))
        else:
            command = input()
            continue

    command = input()

groceries = ", ".join([str(x) for x in shopping_list])
print(groceries)
