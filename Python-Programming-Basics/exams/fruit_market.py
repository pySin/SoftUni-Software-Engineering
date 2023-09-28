# Fruit Market

# Цена на ягодите в лева – реално число в интервала [0.00 … 10000.00]
# Количество на бананите в килограми – реално число в интервала [0.00 … 1 0000.00]
# Количество на портокалите в килограми – реално число в интервала [0.00 … 10000.00]
# Количество на малините в килограми – реално число в интервала [0.00 … 10000.00]
# Количество на ягодите в килограми – реално число в интервала [0.00 … 10000.00]

strawberries_price = float(input())
bananas_amount = float(input())
oranges_amount = float(input())
raspberries_amount = float(input())
strawberries_amount = float(input())

strawberries_sum = strawberries_amount * strawberries_price
raspberries_sum = raspberries_amount * (strawberries_price * 0.50)
oranges_sum = oranges_amount * ((strawberries_price * 0.50) * (1 - 0.40))
bananas_sum = bananas_amount * ((strawberries_price * 0.50) * (1 - 0.80))

whole_sum = strawberries_sum + raspberries_sum + oranges_sum + bananas_sum

print(f"{whole_sum :.2f}")
