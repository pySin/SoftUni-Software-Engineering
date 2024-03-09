# Chicken snack
from collections import deque


money = [int(m) for m in input().split()]
prices = deque([int(p) for p in input().split()])


foods_eaten = 0
while money and prices:

    current_money = money.pop()
    current_price = prices.popleft()

    if current_money == current_price:
        foods_eaten += 1
        continue
    elif current_price > current_money:
        continue
    elif current_money > current_price:
        foods_eaten += 1
        difference = current_money - current_price
        if money:
            money[-1] += difference
        # else:
        #     money.append(difference)

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")
elif foods_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {foods_eaten} foods.")
