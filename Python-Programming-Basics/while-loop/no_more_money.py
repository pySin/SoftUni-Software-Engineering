# No More Money

full_sum = 0
installment = input()

while installment != "NoMoreMoney":

    if float(installment) < 0:
        print(f"Invalid operation!")
        break

    full_sum += float(installment)

    if float(installment) > 0:
        print(f"Increase: {float(installment) :.2f}")
    installment = input()
print(f"Total: {full_sum :.2f}")
