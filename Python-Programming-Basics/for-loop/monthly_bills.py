# Monthly Bills
INTERNET_PRICE = 15
WATER_PRICE = 20

electricity_all = 0
water_all = 0
internet_all = 0
other_all = 0


# Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]

months_count = int(input())

for _ in range(months_count):

    electricity_price = float(input())
    others_price = (electricity_price + WATER_PRICE + INTERNET_PRICE)
    electricity_all += electricity_price
    water_all += WATER_PRICE
    internet_all += INTERNET_PRICE
    other_all += others_price + (others_price * 0.20)

all_expenses = electricity_all + water_all + internet_all + other_all

print(f"Electricity: {electricity_all :.2f} lv")
print(f"Water: {water_all :.2f} lv")
print(f"Internet: {internet_all :.2f} lv")
print(f"Other: {other_all :.2f} lv")
print(f"Average: {all_expenses / months_count :.2f} lv")
