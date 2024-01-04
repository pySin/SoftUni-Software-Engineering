# Fancy Barcodes
import re


def find_matches(barcode):
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    match = re.findall(pattern, barcode)
    if match:
        product_group = "".join([char for char in match[0][1] if char.isdigit()])
        if not product_group:
            print("Product group: 00")
        else:
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")


def call_functions():
    n = int(input())

    for _ in range(n):
        barcode = input()
        find_matches(barcode)


if __name__ == "__main__":
    call_functions()
