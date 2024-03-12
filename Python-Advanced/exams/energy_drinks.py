# Energy Drinks
from collections import deque


MAXIMUM_CAFFEINE = 300

caffeine = [int(c) for c in input().split(", ")]
energy_drinks = deque(int(ed) for ed in input().split(", "))

caffeine_drank = 0
while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_caffeine * current_energy_drink
    if result + caffeine_drank <= MAXIMUM_CAFFEINE:
        caffeine_drank += result
    else:
        energy_drinks.append(current_energy_drink)
        if caffeine_drank - 30 < 0:
            caffeine_drank = 0
        else:
            caffeine_drank -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(ed) for ed in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_drank} mg caffeine.")
