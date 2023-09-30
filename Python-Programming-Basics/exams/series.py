# Series

# Бюджет  - реално  число в интервала [10.0… 100.0]
# Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# Име на сериал - текст
# Цена за сериал -  реално  число в интервала [1.0… 15.0]

budget = float(input())
series_count = int(input())

amount_due = 0

for _ in range(series_count):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price *= 0.50
    elif series_name == "Lucifer":
        series_price *= 0.60
    elif series_name == "Protector":
        series_price *= 0.70
    elif series_name == "TotalDrama":
        series_price *= 0.80
    elif series_name == "Area":
        series_price *= 0.90

    amount_due += series_price

if budget >= amount_due:
    print(f"You bought all the series and left with {budget - amount_due :.2f} lv.")
else:
    print(f"You need {amount_due - budget :.2f} lv. more to buy the series!")
