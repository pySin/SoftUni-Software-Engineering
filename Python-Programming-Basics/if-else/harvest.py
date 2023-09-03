# Harvest
from math import ceil, floor

# 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# 2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# 4ти ред: брой работници – цяло число в интервала [1 … 20]

square_meters = int(input())
grapes_per_meter = float(input())
wine_liters_needed = int(input())
number_of_workers = int(input())

grapes_harvest = square_meters * grapes_per_meter
grapes_for_wine = grapes_harvest * 0.40

wine_liters = grapes_for_wine / 2.50

if wine_liters_needed > wine_liters:
    insufficient_wine = floor(wine_liters_needed - wine_liters)
    print(f"It will be a tough winter! More {insufficient_wine} liters wine needed.")
else:
    wine_left = wine_liters - wine_liters_needed
    wine_per_worker = wine_left / number_of_workers
    print(f"Good harvest this year! Total wine: {ceil(wine_liters)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.")
