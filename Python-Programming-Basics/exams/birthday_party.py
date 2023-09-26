# Birthday Party

# Наем за залата – реално число в интервала [100.00..10000.00]

hall_hire = float(input())

cake_price = hall_hire * 0.20
drinks_price = cake_price * 0.55
animator_price = hall_hire / 3

full_price = hall_hire + cake_price + drinks_price + animator_price
print(f"{full_price}")
