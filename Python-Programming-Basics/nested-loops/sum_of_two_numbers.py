# sum Of Two numbers

# · Първи ред – начало на интервала – цяло число в интервала [1...999]
# · Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# · Трети ред – магическото число – цяло число в интервала [1...10000]

interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
combinations = 0

is_found = False
for number in range(interval_start, interval_end + 1):
    for number_2 in range(interval_start, interval_end + 1):
        combinations += 1
        if number + number_2 == magic_number:
            print(f"Combination N:{combinations} ({number} + {number_2} = {magic_number})")
            is_found = True
    if is_found:
        break

if not is_found:
    print(f"{combinations} combinations - neither equals {magic_number}")
