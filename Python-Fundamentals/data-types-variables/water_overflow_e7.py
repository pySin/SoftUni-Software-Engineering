# Water Overflow

TANK_CAPACITY = 255

number_of_pours = int(input())
tank_fullness = 0

for pour in range(number_of_pours):
    current_pour_liters = int(input())

    if current_pour_liters + tank_fullness > TANK_CAPACITY:
        print("Insufficient capacity!")
        continue
    else:
        tank_fullness += current_pour_liters

print(tank_fullness)
