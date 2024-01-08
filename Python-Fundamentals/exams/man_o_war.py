# Man O War


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]

maximum_health_capacity = int(input())

command = input()

is_ship_sunk = False
while command != "Retire":

    instructions = command.split()

    if instructions[0] == "Fire":
        if int(instructions[1]) not in range(len(warship)):
            command = input()
            continue

        warship[int(instructions[1])] -= int(instructions[2])
        if warship[int(instructions[1])] <= 0:
            is_ship_sunk = True
            print("You won! The enemy ship has sunken.")
            break

    elif instructions[0] == "Defend":
        if int(instructions[1]) not in range(len(pirate_ship)) or\
                int(instructions[2]) not in range(len(pirate_ship) + 1):
            command = input()
            continue

        for i in range(int(instructions[1]), int(instructions[2]) + 1):
            pirate_ship[i] -= int(instructions[3])
            if pirate_ship[i] <= 0:
                is_ship_sunk = True
                print("You lost! The pirate ship has sunken.")
                break

    elif instructions[0] == "Repair":
        if int(instructions[1]) not in range(len(pirate_ship)):
            command = input()
            continue

        if pirate_ship[int(instructions[1])] + int(instructions[2]) > maximum_health_capacity:
            pirate_ship[int(instructions[1])] = maximum_health_capacity
        else:
            pirate_ship[int(instructions[1])] += int(instructions[2])

    elif instructions[0] == "Status":
        critical_health = maximum_health_capacity * 0.2
        # print(critical_health)
        critical_sections_count = 0
        for item in pirate_ship:
            if item < critical_health:
                critical_sections_count += 1

        print(f"{critical_sections_count} sections need repair.")

    command = input()

if not is_ship_sunk:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
