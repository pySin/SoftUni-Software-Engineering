# Family Trip

# Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
# Брой нощувки – цяло число в интервала [0 … 1000]
# Цена за нощувка – реално число в интервала [1.00 … 500.00]
# Процент за допълнителни разходи – цяло число в интервала [0 … 100]

budget = float(input())
number_of_stays = int(input())
price_per_night = float(input())
additional_expenses_percent = float(input())

expenses = 0

if number_of_stays > 7:
    expenses = ((number_of_stays * price_per_night) * 0.95) \
               + budget * (additional_expenses_percent / 100)
else:
    expenses = (number_of_stays * price_per_night)\
               + (budget * (additional_expenses_percent / 100))

if budget >= expenses:
    print(f"Ivanovi will be left with {budget - expenses :.2f} leva after vacation.")
else:
    print(f"{expenses - budget :.2f} leva needed.")
