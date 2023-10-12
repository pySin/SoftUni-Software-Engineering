# Shopping

budget = int(input())

product = input()
amount_due = 0

is_overdraft = False
while not product == "End":
    product_int = int(product)

    amount_due += product_int
    if amount_due > budget:
        is_overdraft = True
        print("You went in overdraft!")
        break

    product = input()

if not is_overdraft:
    print("You bought everything needed.")
