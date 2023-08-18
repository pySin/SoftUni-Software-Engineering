# Movie Voucher

voucher_amount = int(input())
tickets_count = 0
goods_count = 0

while True:
    product = input()
    product_price = 0
    if len(product) >= 8:
        product_price = ord(product[0]) + ord(product[1])
        if product_price > voucher_amount or product == "End":
            break
        else:
            print(product_price)
            voucher_amount = voucher_amount - product_price
            tickets_count += 1
    else:
        product_price = ord(product[0])
        if product_price > voucher_amount or product == "End":
            break
        else:
            voucher_amount = voucher_amount - product_price
            goods_count += 1
            print(product_price)

print(tickets_count)
print(goods_count)
