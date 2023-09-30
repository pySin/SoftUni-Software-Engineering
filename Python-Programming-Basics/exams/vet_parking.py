# Vet Parking

# Брой дни – цяло число в интервала [1 … 5]
# Брой часове за всеки един от дните - цяло число в интервала [1 … 24]

days = int(input())
hours = int(input())
bill = 0

x = 0
while x < days:
    x += 1

    day_bill = 0
    y = 0
    while y < hours:
        y += 1
        if x % 2 == 0 and y % 2 != 0:
            day_bill += 2.50
        elif x % 2 != 0 and y % 2 == 0:
            day_bill += 1.25
        else:
            day_bill += 1
    print(f"Day: {x} - {day_bill :.2f} leva")
    bill += day_bill

print(f"Total: {bill :.2f} leva")
