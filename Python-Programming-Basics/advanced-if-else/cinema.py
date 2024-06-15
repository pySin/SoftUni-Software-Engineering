# Cinema

# ⦁	Premiere - премиерна прожекция, на цена 12.00 лева;
# ⦁	Normal - стандартна прожекция, на цена 7.50 лева;
# ⦁	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.


screening_type = input()  # Premiere, Normal, Discount
rows = int(input())
columns = int(input())

price = 0

if screening_type == "Premiere":
    price = 12
if screening_type == "Normal":
    price = 7.50
if screening_type == "Discount":
    price = 5.00

income = (rows * columns) * price
print(f"{income :.2f} leva")


