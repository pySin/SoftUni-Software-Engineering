# Find The discount

full_price = int(input())
discount_amount = int(input())


def dis(price, discount):
    return price - (price * (discount / 100))


get_discount = dis(full_price, discount_amount)
print(get_discount)
