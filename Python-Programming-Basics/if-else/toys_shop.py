# Toys Shop

PUZZLE = 2.60
TALKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
SMALL_TRUCK = 2

trip_price = float(input())
puzzle_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

income = PUZZLE * puzzle_count + TALKING_DOLL * talking_dolls_count + TEDDY_BEAR * teddy_bears_count \
    + MINION * minions_count + SMALL_TRUCK * trucks_count

order_count = puzzle_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

if order_count >= 50:
    income *= 1 - 0.25

income *= 1 - 0.10
remainder = income - trip_price

if remainder >= 0:
    print(f"Yes! {remainder :.2f} lv left.")
else:
    print(f"Not enough money! {abs(remainder) :.2f} lv needed.")
    print(f"Increase: {installment:.2f}")
