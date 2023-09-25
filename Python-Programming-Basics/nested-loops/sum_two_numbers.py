# Sum Of Two Numbers

# ⦁	Първи ред – начало на интервала – цяло число в интервала [1...999]
# ⦁	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# ⦁	Трети ред – магическото число – цяло число в интервала [1...10000]

interval_start = int(input())
interval_finish = int(input())
magic_number = int(input())

first_number = 0
second_number = 0

combinations = 0
is_found = False
for i in range(interval_start, interval_finish + 1):
    for j in range(interval_start, interval_finish + 1):
        combinations += 1
        if i + j == magic_number:
            first_number = i
            second_number = j
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")
