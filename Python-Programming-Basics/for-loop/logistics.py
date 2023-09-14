# Logistics

# На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]

cargo_count = int(input())

whole_cargo_weight = 0
amount_due = 0
bus_cargo = 0
truck_cargo = 0
train_cargo = 0

for _ in range(cargo_count):
    cargo_weight = int(input())
    whole_cargo_weight += cargo_weight

    if cargo_weight <= 3:
        amount_due += cargo_weight * 200
        bus_cargo += cargo_weight
    elif 4 <= cargo_weight <= 11:
        amount_due += cargo_weight * 175
        truck_cargo += cargo_weight
    elif cargo_weight > 11:
        amount_due += cargo_weight * 120
        train_cargo += cargo_weight

print(f"{amount_due / whole_cargo_weight :.2f}")
print(f"{(bus_cargo / whole_cargo_weight) * 100 :.2f}%")
print(f"{(truck_cargo / whole_cargo_weight) * 100 :.2f}%")
print(f"{(train_cargo / whole_cargo_weight) * 100 :.2f}%")
