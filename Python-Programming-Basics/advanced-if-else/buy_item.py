# Buy Item

product = input()
town = input()
amount = float(input())


bill = 0
if town == "Sofia":
    if product == "coffee":
        bill = amount * 0.50
    elif product == "water":
        bill = amount * 0.80
    elif product == "beer":
        bill = amount * 1.20
    elif product == "sweets":
        bill = amount * 1.45
    elif product == "peanuts":
        bill = amount * 1.60

if town == "Plovdiv":
    if product == "coffee":
        bill = amount * 0.40
    elif product == "water":
        bill = amount * 0.70
    elif product == "beer":
        bill = amount * 1.15
    elif product == "sweets":
        bill = amount * 1.30
    elif product == "peanuts":
        bill = amount * 1.50

if town == "Varna":
    if product == "coffee":
        bill = amount * 0.45
    elif product == "water":
        bill = amount * 0.70
    elif product == "beer":
        bill = amount * 1.10
    elif product == "sweets":
        bill = amount * 1.35
    elif product == "peanuts":
        bill = amount * 1.55

print(f"{bill}")
