# Cinema Ticket

cinema_day = input()

price = 0
if cinema_day == "Monday" or cinema_day == "Tuesday" or cinema_day == "Friday":
    price = 12
elif cinema_day == "Wednesday" or cinema_day == "Thursday":
    price = 14
else:
    price = 16

print(price)
