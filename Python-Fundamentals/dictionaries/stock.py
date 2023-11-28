# Stock

pairs = {}


def stocks(products):

    products = products.split()
    for i in range(0, len(products), 2):
        pairs[products[i]] = products[i + 1]


products_options = input()
stocks(products_options)

needed_products = input().split()
for product in needed_products:
    if product in pairs.keys():
        print(f"We have {pairs[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
