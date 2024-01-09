# Moving Target

def shoot(event, target_row):
    target_row[int(event[1])] -= int(event[2])
    if target_row[int(event[1])] <= 0:
        target_row.pop(int(event[1]))
    return target_row


def add(event, target_row):
    if int(event[1]) in range(len(target_row)):
        target_row.insert(int(event[1]), int(event[2]))
    else:
        print("Invalid placement!")
    return target_row


def strike(event, target_row):
    strike_index = int(event[1])
    strike_radius = int(event[2])
    if strike_index - strike_radius < 0 or strike_index + strike_radius > len(target_row) - 1:
        print("Strike missed!")
    else:
        target_row = target_row[0: strike_index - strike_radius] + target_row[strike_index + strike_radius + 1:]
    return target_row


targets_row = [int(target_x) for target_x in input().split()]


def change_targets(targets):
    command = input()

    while command != "End":

        event = command.split()

        if event[0] == "Shoot":
            targets = shoot(event, targets)
        elif event[0] == "Add":
            targets = add(event, targets)
        elif event[0] == "Strike":
            targets = strike(event, targets)

        command = input()
    divided_targets = "|".join(map(str, targets))
    print(f"{divided_targets}")


change_targets(targets_row)
