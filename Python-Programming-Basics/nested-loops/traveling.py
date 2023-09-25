# Traveling

destination = input()
money_saved = 0

while destination != "End":
    money_needed = float(input())
    while money_needed > money_saved:
        current_saving = float(input())
        money_saved += current_saving
    print(f"Going to {destination}!")
    money_saved = 0
    destination = input()
