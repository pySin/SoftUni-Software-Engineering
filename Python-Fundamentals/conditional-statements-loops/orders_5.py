# Orders

number_of_orders = int(input())
amount_due = 0

for i in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100.00 or not 0 < days <= 31 or not 1 <= capsules_per_day <= 2000:
        continue

    price_for_coffe = price_per_capsule * days * capsules_per_day
    amount_due += price_for_coffe

    print(f"The price for the coffee is: ${price_for_coffe :.2f}")

print(f"Total: ${amount_due :.2f}")
