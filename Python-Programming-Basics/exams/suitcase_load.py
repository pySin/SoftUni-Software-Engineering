# Suitcase load

# Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
# След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# Обем на куфар – реално число в диапазона [100.0…6000.0]

trunk_capacity = float(input())

size_filled = 0
suitcases_count = 0

x = 0
while True:
    x += 1
    suitcase_size = input()

    if suitcase_size == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break

    suitcase_size = float(suitcase_size)

    if x % 3 == 0:
        suitcase_size *= 1.10

    size_filled += suitcase_size

    if size_filled > trunk_capacity:
        print(f"No more space!")
        break

    suitcases_count += 1

print(f"Statistic: {suitcases_count} suitcases loaded.")
