# Counter Strike


initial_energy = int(input())

command = input()
won_battles = 0

is_energy_not_enough = False
while command != "End of battle":

    distance = int(command)

    if distance > initial_energy:
        is_energy_not_enough = True
        break
    else:
        initial_energy -= distance

    won_battles += 1

    if won_battles % 3 == 0:
        initial_energy += won_battles

    command = input()

if is_energy_not_enough:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
