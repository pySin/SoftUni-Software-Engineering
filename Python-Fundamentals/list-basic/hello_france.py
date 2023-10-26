# Hello France

TARGET_BUDGET = 150

items_to_buy = input().split("|")
initial_budget = float(input())
budget = initial_budget

expenses = 0

is_budget_over = False
while True:

    new_item_prices = []

    for buy_item in items_to_buy:
        item_name, item_price = buy_item.split("->")
        item_price = float(item_price)
        # print(item_price)
        if item_name == "Clothes" and item_price > 50.00:
            continue
        elif item_name == "Shoes" and item_price > 35.00:
            continue
        elif item_name == "Accessories" and item_price > 20.50:
            continue

        # print(item_price)
        # print(budget)
        # print(buy_item)
        if budget >= item_price:
            # print(item_price)
            budget -= item_price
            expenses += item_price
            new_item_prices.append(round(item_price * 1.40, 2))
        elif budget < item_price:
            is_budget_over = True
            break
        elif items_to_buy.index(buy_item) + 1 == len(items_to_buy):
            is_budget_over = True
            break
        else:
            continue

    if is_budget_over:
        break


new_budget = budget + sum(new_item_prices)
if new_budget >= TARGET_BUDGET:
    print(" ".join(list(map(str, new_item_prices))))
    print(f"Profit: {new_budget - initial_budget :.2f}")
    print("Hello, France!")
else:
    print(" ".join(list(map(str, new_item_prices))))
    print(f"Profit: {new_budget - initial_budget :.2f}")
    print("Not enough money.")
