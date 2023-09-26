# Change Bureau

# На първия ред – броят биткойни. Цяло число в интервала [0…20]
# На втория ред – броят китайски юана. Реално число в интервала [0.00… 50 000.00]
# На третия ред – комисионната. Реално число в интервала [0.00 ... 5.00]

bitcoins_amount = int(input())
iuans_count = float(input())
interest = float(input())

euro_from_bitcoin = (bitcoins_amount * 1168) / 1.95
euro_from_iuan = ((iuans_count * 0.15) * 1.76) / 1.95

all_euro = euro_from_bitcoin + euro_from_iuan
all_euro = all_euro * (1 - (interest / 100))
print(f"{all_euro :.2f}")
