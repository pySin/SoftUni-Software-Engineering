# Flower Purchase
from math import floor, ceil


# Магнолии – 3.25 лева
# Зюмбюли – 4 лева
# Рози – 3.50 лева
# Кактуси – 8 лева

MAGNOLIA = 3.25
HYACINTH = 4
ROSE = 3.50
CACTUS = 8

# Брой магнолии – цяло число в интервала [0 … 50]
# Брой зюмбюли – цяло число в интервала [0 … 50]
# Брой рози – цяло число в интервала [0 … 50]
# Брой кактуси – цяло число в интервала [0 … 50]
# Цена на подаръка – реално число в интервала [0.00 … 500.00]

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

purchase_amount = magnolias_count * MAGNOLIA + hyacinths_count * HYACINTH \
                  + roses_count * ROSE + cactus_count * CACTUS
sum_after_tax = purchase_amount * (1 - 0.05)

if gift_price > sum_after_tax:
    print(f"She will have to borrow {ceil(gift_price - sum_after_tax)} leva.")
else:
    print(f"She is left with {floor(sum_after_tax - gift_price)} leva.")
