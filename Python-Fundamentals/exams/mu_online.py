# Mu Online


dungeon_rooms = input().split("|")

health = 100
bitcoins = 0

room_number = 0

is_health_over = False
for i in range(len(dungeon_rooms)):

    instruction = dungeon_rooms[i].split()
    room_number += 1

    command = instruction[0]
    number = int(instruction[1])

    if command == "potion":
        current_health = health
        if health + number >= 100:
            health = 100
            print(f"You healed for {100 - current_health} hp.")
        else:
            health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        elif health <= 0:
            is_health_over = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            break

if not is_health_over:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
