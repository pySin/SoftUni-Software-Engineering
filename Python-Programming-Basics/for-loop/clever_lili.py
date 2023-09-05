# Clever Lili

# ⦁	Възрастта на Лили - цяло число в интервала [1...77]
# ⦁	Цената на пералнята - число в интервала [1.00...10 000.00]
# ⦁	Единична цена на играчка - цяло число в интервала [0...40]

lili_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

number_of_toys = 0
birthday_money = 0
money_collected = 0

for i in range(1, lili_age + 1):
    if i % 2 != 0:
        number_of_toys += 1
    elif i % 2 == 0:
        birthday_money += 10
        money_collected += birthday_money

brother_money = lili_age // 2
money_collected += number_of_toys * toy_price
money_collected -= brother_money
remainder = money_collected - washing_machine_price

if remainder >= 0:
    print(f"Yes! {remainder :.2f}")
else:
    print(f"No! {abs(remainder) :.2f}")
