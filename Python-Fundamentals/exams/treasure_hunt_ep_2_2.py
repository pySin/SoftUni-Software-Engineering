# Treasure Hunt
# Get the initial loot and change it to a list.
# Create a function with parameter the initial loot.
# Start accepting commands for events.
# After each event check the type of event.
# For each type of event apply different functionality.
# Print a phrase if the treasure chest is empty.
# Calculate and print the average treasure gain.

initial_loot = input().split("|")


def looting(chest_state):
    command = input()
    phrases = []

    while command != "Yohoho!":

        event = command.split()
        if event[0] == "Loot":
            for item in event[1:]:
                if item not in chest_state:
                    chest_state.insert(0, item)
        elif event[0] == "Drop":
            if abs(int(event[1])) < len(chest_state):
                chest_state.append(chest_state.pop(int(event[1])))
        elif event[0] == "Steal":
            stolen_items = chest_state[-int(event[1]):]
            print(*stolen_items)
            [chest_state.pop() for x in range(int(event[1])) if chest_state]
        command = input()

    if not chest_state:
        print(f"Failed treasure hunt.")
    else:

        treasure_gain = [len(item) for item in chest_state]
        treasure_gain = sum(treasure_gain) / len(chest_state)
        print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")


looting(initial_loot)
