# Apocalypse Preparation
from collections import deque


textiles = deque([int(t) for t in input().split()])
medicaments = [int(m) for m in input().split()]

patch = 30
bandage = 40
med_kit = 100

patch_count = ["Patch", 0]
bandage_count = ["Bandage", 0]
med_kit_count = ["MedKit", 0]

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    current_sum = current_textile + current_medicament

    if current_sum == patch:
        patch_count[1] += 1
    elif current_sum == bandage:
        bandage_count[1] += 1
    elif current_sum == med_kit:
        med_kit_count[1] += 1
    elif current_sum > med_kit:
        med_kit_count[1] += 1
        last_medicament = medicaments.pop() + (current_sum - med_kit)
        medicaments.append(last_medicament)
    else:
        medicaments.append(current_medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

created_items = sorted([patch_count, bandage_count, med_kit_count], key=lambda x: (-x[1], x[0]))
for item in created_items:
    if item[1] > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(m) for m in medicaments][::-1])}")
elif textiles:
    print(f"Textiles left: {', '.join([str(t) for t in textiles])}")
