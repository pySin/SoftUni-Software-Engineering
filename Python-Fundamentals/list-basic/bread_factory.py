# Bread factory

INITIAL_ENERGY = 100
INITIAL_COINS = 100

day_events = input().split("|")
# print(day_events)

is_money_not_enough = False
for event in day_events:
    if "rest" in event:
        minutes_rest = int(event[5:])
        minutes_gained = 0
        if INITIAL_ENERGY + minutes_rest > 100:
            minutes_gained = 100 - INITIAL_ENERGY
            print(f"You gained {minutes_gained} energy.")
            print(f"Current energy: {INITIAL_ENERGY}.")
        else:
            INITIAL_ENERGY += minutes_rest
            print(f"You gained {minutes_rest} energy.")
            print(f"Current energy: {INITIAL_ENERGY}.")
    elif "order" in event:
        if INITIAL_ENERGY >= 30:
            INITIAL_ENERGY -= 30
            coins_earned = int(event[6:])
            INITIAL_COINS += coins_earned
            print(f"You earned {coins_earned} coins.")
        else:
            INITIAL_ENERGY += 50
            print("You had to rest!")
    else:
        delimiter_index = event.index("-")
        ingredient = event[:delimiter_index]
        money_for_product = int(event[delimiter_index + 1:])
        if INITIAL_COINS >= money_for_product:
            INITIAL_COINS -= money_for_product
            print(f"You bought {ingredient}.")
        else:
            is_money_not_enough = True
            print(f"Closed! Cannot afford {ingredient}.")
            break


if not is_money_not_enough:
    print(f"Day completed!")
    print(f"Coins: {INITIAL_COINS}")
    print(f"Energy: {INITIAL_ENERGY}")
