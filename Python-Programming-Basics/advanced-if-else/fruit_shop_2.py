# Fruit Shop 2

item = input()
day = input()
quantity = float(input())

bill = 0
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if item == "banana":
        bill = quantity * 2.50
    elif item == "apple":
        bill = quantity * 1.20
    elif item == "orange":
        bill = quantity * 0.85
    elif item == "grapefruit":
        bill = quantity * 1.45
    elif item == "kiwi":
        bill = quantity * 2.70
    elif item == "pineapple":
        bill = quantity * 5.50
    elif item == "grapes":
        bill = quantity * 3.85
elif day == "Saturday" or day == "Sunday":
    if item == "banana":
        bill = quantity * 2.70
    elif item == "apple":
        bill = quantity * 1.25
    elif item == "orange":
        bill = quantity * 0.90
    elif item == "grapefruit":
        bill = quantity * 1.60
    elif item == "kiwi":
        bill = quantity * 3.00
    elif item == "pineapple":
        bill = quantity * 5.60
    elif item == "grapes":
        bill = quantity * 4.20

if bill == 0:
    print("error")
else:
    print(f"{bill :.2f}")
