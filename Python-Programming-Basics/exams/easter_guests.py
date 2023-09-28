# Easter Guests
from math import ceil


# На първия ред са броят на гостите – цяло число в интервала [0 ... 200000]
# На втория ред е бюджетът с който разполага Любо  – цяло число в интервала [0 ... 200000]

guests_amount = int(input())
budget = int(input())

sweet_breads = ceil(guests_amount / 3)
sweet_breads_bill = sweet_breads * 4
eggs_amount = guests_amount * 2
eggs_bill = eggs_amount * 0.45

bill = sweet_breads_bill + eggs_bill

if budget >= bill:
    print(f"Lyubo bought {sweet_breads} Easter bread and {eggs_amount} eggs.")
    print(f"He has {budget - bill :.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {bill - budget :.2f} lv. more.")
