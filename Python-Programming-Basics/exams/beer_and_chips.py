# Beer and chips
from math import ceil

# На първия ред - името на футболният фен – текст
# На втория ред - предвиденият бюджет  – реално число в диапазона [1.0… 100 000.0]
# На третия ред - брой бутилки бира – цяло число в диапазона [1… 100 000]
# На четвърти ред - брой пакети чипс – цяло число в диапазона [1… 100 000]

BEER_PRICE = 1.20


fan_name = input()
budget = float(input())
beers_count = int(input())
chips_count = int(input())

beers_bill = beers_count * BEER_PRICE
chips_price = beers_bill * 0.45

chips_bill = ceil(chips_count * chips_price)
full_bill = beers_bill + chips_bill

if full_bill > budget:
    print(f"{fan_name} needs {full_bill - budget :.2f} more leva!")
else:
    print(f"{fan_name} bought a snack and has {budget - full_bill :.2f} leva left.")
