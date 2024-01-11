# Shoot for the win


targets = [int(x) for x in input().split()]
shot_targets = 0

command = input()

while command != "End":

    shot_index = int(command)

    if shot_index > (len(targets) - 1):
        command = input()
        continue
    elif targets[shot_index] == - 1:
        command = input()
        continue

    index_value = targets[shot_index]

    targets[shot_index] = -1
    shot_targets += 1

    for i in range(len(targets)):
        if targets[i] == -1 or i == shot_index:
            continue
        else:
            if targets[i] > index_value:
                targets[i] = targets[i] - index_value
            elif targets[i] <= index_value:
                targets[i] = targets[i] + index_value

    command = input()

targets_print = " ".join(map(str, targets))
print(f"Shot targets: {shot_targets} -> {targets_print}")
