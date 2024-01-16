# Treasure Hunt


initial_loot = input().split("|")

command = input()

while command != "Yohoho!":

    instructions = command.split()

    if instructions[0] == "Loot":

        for i in range(1, len(instructions)):
            if instructions[i] in initial_loot:
                continue
            else:
                initial_loot.insert(0, instructions[i])

    elif instructions[0] == "Drop":
        if int(instructions[1]) in range(len(initial_loot)):
            initial_loot.append(initial_loot.pop(int(instructions[1])))

    elif instructions[0] == "Steal":
        stolen_loot = []
        for _ in range(int(instructions[1])):
            if len(initial_loot) > 0:
                stolen_loot.insert(0, initial_loot.pop())
        print(", ".join(stolen_loot))
    command = input()

items_lengths = list(map(len, initial_loot))
if len(initial_loot) > 0:
    treasure_gain = sum(items_lengths) / len(items_lengths)
else:
    treasure_gain = 0

if len(initial_loot) < 1:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")
