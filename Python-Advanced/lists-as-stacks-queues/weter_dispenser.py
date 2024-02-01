# Water Dispenser
from collections import deque

water_quantity = int(input())
thirsty_people = deque()

while True:
    command = input()
    if command != "Start":
        thirsty_people.append(command)
    else:
        break

while True:
    command_2 = input()
    if command_2 == "End":
        print(f"{water_quantity} liters left")
        break
    elif command_2.isdigit():
        current_liters = int(command_2)
        if water_quantity >= current_liters:
            water_quantity -= current_liters
            queue_person = thirsty_people.popleft()
            print(f"{queue_person} got water")
        elif water_quantity < current_liters:
            queue_person = thirsty_people[0]
            print(f"{queue_person} must wait")
    elif command_2.split(" ")[0] == "refill":
        water_quantity += int(command_2.split(" ")[1])
