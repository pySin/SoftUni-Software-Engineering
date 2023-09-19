# Happy Cat Parking


# ⦁	Брой дни – цяло число в интервала [1 … 5]
# ⦁	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]

day_count = int(input())
hours_count = int(input())

whole_sum = 0

for day in range(1, day_count + 1):
    days_sum = 0
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            days_sum += 2.50
            whole_sum += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            days_sum += 1.25
            whole_sum += 1.25
        else:
            days_sum += 1.00
            whole_sum += 1.00
    print(f"Day: {day} - {days_sum:.2f} leva")

print(f"Total: {whole_sum:.2f} leva")
