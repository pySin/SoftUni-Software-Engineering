# Milkshakes
from collections import deque


chocolate_portions = deque([int(x) for x in input().split(", ")])
milk_portions = deque([int(x) for x in input().split(", ")])

milkshakes_made = 0

while True:

    if milkshakes_made == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break
    elif len(chocolate_portions) <= 0 or len(milk_portions) <= 0:
        print("Not enough milkshakes.")
        break

    if chocolate_portions[-1] <= 0:
        chocolate_portions.pop()
        continue

    if milk_portions[0] <= 0:
        milk_portions.popleft()
        continue

    last_chocolate = chocolate_portions.pop()
    first_milk = milk_portions.popleft()

    if last_chocolate == first_milk:
        milkshakes_made += 1
    else:
        milk_portions.append(first_milk)
        chocolate_portions.append(last_chocolate - 5)


if len(chocolate_portions) <= 0 or chocolate_portions[0] <= 0:
    print("Chocolate: empty")
else:
    chocolate_left = ", ".join([str(x) for x in chocolate_portions])
    print(f"Chocolate: {chocolate_left}")

if len(milk_portions) <= 0 or milk_portions[0] <= 0:
    milk_left = str(milk_portions)
    print("Milk: empty")
else:
    milk_left = ", ".join([str(x) for x in milk_portions])
    print(f"Milk: {milk_left}")
