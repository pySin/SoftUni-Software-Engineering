# Easter gifts


gifts = input().split()
command = input()

while command != "No Money":

    command_details = command.split()
    if command_details[0] == "OutOfStock":
        if command_details[1] in gifts:
            for i in range(len(gifts)):
                if gifts[i] == command_details[1]:
                    gifts[i] = "None"

    elif command_details[0] == "Required":
        if int(command_details[2]) in range(len(gifts)):
            gifts[int(command_details[2])] = command_details[1]

    elif command_details[0] == "JustInCase":
        gifts[-1] = command_details[1]

    command = input()

for item in gifts:
    if item != "None":
        print(item, end=" ")
