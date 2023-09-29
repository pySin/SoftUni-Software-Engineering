# Movie Destination

# Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# Сезон – текст, с възможности "Summer" и "Winter"
# Брой дни  – цяло число в диапазона [1… 40]

budget = float(input())
destination = input()
season = input()
days = int(input())

bill = 0

if season == "Winter":
    if destination == "Dubai":
        bill = (days * 45000) * 0.70
    elif destination == "Sofia":
        bill = (days * 17000) * 1.25
    else:
        bill = days * 24000
elif season == "Summer":
    if destination == "Dubai":
        bill = (days * 40000) * 0.70
    elif destination == "Sofia":
        bill = (days * 12500) * 1.25
    else:
        bill = days * 20250

if budget >= bill:
    print(f"The budget for the movie is enough! We have {budget - bill :.2f} leva left!")
else:
    print(f"The director needs {bill - budget :.2f} leva more!")
