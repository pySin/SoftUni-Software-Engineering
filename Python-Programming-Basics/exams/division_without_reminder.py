# Division Without Reminder

numbers_amount = int(input())
p1 = 0
p2 = 0
p3 = 0


x = 0
while x < numbers_amount:
    x += 1

    number = int(input())
    if number % 2 == 0:
        p1 += 1

    if number % 3 == 0:
        p2 += 1

    if number % 4 == 0:
        p3 += 1

print(f"{(p1 / numbers_amount) * 100 :.2f}%")
print(f"{(p2 / numbers_amount) * 100 :.2f}%")
print(f"{(p3 / numbers_amount) * 100 :.2f}%")
