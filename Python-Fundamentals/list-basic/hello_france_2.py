#  Hello France 2

TARGET_BUDGET = 150

items_to_buy = input().split("|")
initial_budget = float(input())
budget = initial_budget

expenses = 0


new_item_prices = []

for buy_item in items_to_buy:
    item_name, item_price = buy_item.split("->")
    item_price = float(item_price)
    if item_name == "Clothes" and item_price > 50.00:
        continue
    elif item_name == "Shoes" and item_price > 35.00:
        continue
    elif item_name == "Accessories" and item_price > 20.50:
        continue

    if budget >= item_price:
        budget -= item_price
        expenses += item_price
        # new_item_prices.append(round(item_price * 1.40, 2))
        new_item_prices.append(item_price * 1.40)

    if budget <= 0:
        break

profit = sum(new_item_prices) - expenses
new_budget = budget + sum(new_item_prices)
if new_budget >= TARGET_BUDGET:
    new_item_prices = " ".join([str(round(item, 2)) for item in new_item_prices])
    print(new_item_prices)
    print(f"Profit: {profit :.2f}")
    print("Hello, France!")
else:
    new_item_prices = " ".join([str(round(item, 2)) for item in new_item_prices])
    print(new_item_prices)
    print(f"Profit: {profit :.2f}")
    print("Not enough money.")
