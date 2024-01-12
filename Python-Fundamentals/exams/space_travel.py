# Space Travel


travel_route_titan = input().split("||")
fuel = int(input())
ammunition = int(input())

for i in range(len(travel_route_titan)):

    current_instruction = travel_route_titan[i].split()

    if current_instruction[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    operation = current_instruction[0]
    amount = int(current_instruction[1])

    if operation == "Travel":
        if amount > fuel:
            print("Mission failed.")
            break
        else:
            print(f"The spaceship travelled {amount} light-years.")
            fuel -= amount

    if operation == "Enemy":
        if amount <= ammunition:
            ammunition -= amount
            print(f"An enemy with {amount} armour is defeated.")
        elif amount * 2 <= fuel:
            fuel -= amount * 2
            print(f"An enemy with {amount} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    if operation == "Repair":
        fuel += amount
        ammunition += amount * 2
        print(f"Ammunitions added: {amount * 2}.")
        print(f"Fuel added: {amount}.")

