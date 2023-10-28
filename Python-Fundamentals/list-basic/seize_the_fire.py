# Seize the fire

fire_cells = input().split("#")
water = int(input())
total_fire = 0
effort = 0

print("Cells:")
for fire_cell in fire_cells:
    type_of_fire, str_level_of_fire = fire_cell.split(" = ")
    level_of_fire = int(str_level_of_fire)

    if type_of_fire == "High" and not 81 <= level_of_fire <= 125:
        continue
    if type_of_fire == "Medium" and not 51 <= level_of_fire <= 80:
        continue
    if type_of_fire == "Low" and not 1 <= level_of_fire <= 50:
        continue

    if water >= level_of_fire:
        total_fire += level_of_fire
        water -= level_of_fire
        print(f" - {level_of_fire}")
        effort += level_of_fire * 0.25

print(f"Effort: {effort :.2f}")
print(f"Total Fire: {total_fire}")
