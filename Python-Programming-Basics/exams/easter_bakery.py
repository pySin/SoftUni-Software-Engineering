# Easter Bakery

# Цена на брашното за един килограм – реално число в интервала [0.00 … 10000.00]
# Килограми на брашното – реално число в интервала [0.00 … 10000.00]
# Килограми на захарта – реално число в интервала [0.00 … 10000.00]
# Брой кори с яйца – цяло число в интервала [0 … 10000]
# Пакети мая  – цяло число в интервала [0 … 10000]

flour_price = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
egg_packs = int(input())
east_packs = int(input())

bill = (flour_kilos * flour_price) + (sugar_kilos * (flour_price * 0.75)) \
       + (egg_packs * (flour_price * 1.10)) + (east_packs * ((flour_price * 0.75) * 0.20))

print(f"{bill :.2f}")
