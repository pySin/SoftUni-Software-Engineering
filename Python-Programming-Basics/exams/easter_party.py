# Easter Party

# Брой гости – цяло число в интервала [1...99]
# Цена на куверт за един човек – реално число в интервала [0.00 … 99.00]
# Бюджетът на Деси  – реално число в интервала [0.00 … 9999.00]

guests_amount = int(input())
entrance_fee = float(input())
budget = float(input())

cake_price = budget * 0.10
entrance_bill = guests_amount * entrance_fee


if 10 <= guests_amount <= 15:
    entrance_bill *= 0.85
elif 15 < guests_amount <= 20:
    entrance_bill *= 0.80
elif guests_amount > 20:
    entrance_bill *= 0.75

full_bill = cake_price + entrance_bill

if budget >= full_bill:
    print(f"It is party time! {budget - full_bill :.2f} leva left.")
else:
    print(f"No party! {full_bill - budget :.2f} leva needed.")
