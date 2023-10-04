# Dynamic Promotion Check

PROMOTION_10_PERCENT_LIMIT = 100
PROMOTION_15_PERCENT_LIMIT = 200
amount_due = 0
final_amount = 0

product_price = 0
while not product_price == "Stop":
    try:
        product_price = input("Insert Product price: ")
        if product_price == "Stop":
            promotion_percentage = 5
            if PROMOTION_10_PERCENT_LIMIT < amount_due < PROMOTION_15_PERCENT_LIMIT:
                promotion_percentage = 10
            elif amount_due > PROMOTION_15_PERCENT_LIMIT:
                promotion_percentage = 15
            print(f"Your promotion is {promotion_percentage}%")
            print(f"Your amount due is: {final_amount}")
            break
        product_price = int(product_price)
    except ValueError:
        print(f"{product_price}")
        print("You must Enter a number or Stop!")
        continue

    amount_due += product_price

    if PROMOTION_15_PERCENT_LIMIT > amount_due >= PROMOTION_10_PERCENT_LIMIT:
        final_amount = amount_due * 0.90
        print("Your promotion is 10%")
        print(f"Your amount due is: {final_amount}")
    elif amount_due >= PROMOTION_15_PERCENT_LIMIT:
        final_amount = amount_due * 0.85
        print("Your promotion is 15%")
        print(f"Your amount due is: {final_amount}")
    elif amount_due < PROMOTION_10_PERCENT_LIMIT:
        final_amount = amount_due * 0.95
        print("Your promotion is 5%")
        print(f"Your amount due is: {final_amount}")
