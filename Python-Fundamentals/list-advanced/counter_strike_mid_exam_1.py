# Counter Strike

initial_energy = int(input())


def strike(energy_available):
    command = input()
    wins_count = 0
    while command != "End of battle":
        current_distance = int(command)

        if current_distance > energy_available:
            return f"Not enough energy! Game ends with {wins_count} won battles and {energy_available} energy"
        else:
            energy_available -= current_distance
            wins_count += 1
            if wins_count % 3 == 0:
                energy_available += wins_count

        command = input()
    return f"Won battles: {wins_count}. Energy left: {energy_available}"


print(strike(initial_energy))
