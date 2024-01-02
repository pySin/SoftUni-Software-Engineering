# Cooking Masterclass
from math import ceil


budget = float(input())
students = int(input())
flour_package_price = float(input())
egg_price = float(input())
apron_price = float(input())


whole_flour_price = flour_package_price * students - ((students // 5) * flour_package_price)
whole_egg_price = (egg_price * 10) * students
whole_apron_price = apron_price * (students + ceil(students * 0.20))

whole_price = whole_flour_price + whole_egg_price + whole_apron_price

if whole_price <= budget:
    print(f"Items purchased for {whole_price:.2f}$.")
else:
    print(f"{whole_price - budget:.2f}$ more needed.")
