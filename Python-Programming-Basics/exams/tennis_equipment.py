# Tennis Equipment
from math import floor, ceil

# "Price to be paid by Djokovic {1/8 от общата цена, закръглена към по-малкото цяло число}"
# "Price to be paid by sponsors {7/8 от общата цена, закръглена към по-голямото цяло число}"

# Цена на една тенис ракета – реално число в интервала [0.00…100000.00]
# Брой тенис ракети - цяло число в интервала [0…100]
# Брой чифтове маратонки - цяло число в интервала [0…100]

tennis_tool = float(input())
tools_amount = int(input())
trainers_amount = int(input())

tools_price = tennis_tool * tools_amount
trainers_price = (tennis_tool / 6) * trainers_amount
total_bill = tools_price + trainers_price
total_bill *= 1.20

print(f"Price to be paid by Djokovic {floor(total_bill / 8)}")
print(f"Price to be paid by sponsors {ceil(total_bill * (7/8))}")
