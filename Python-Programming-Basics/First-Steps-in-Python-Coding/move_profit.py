# Movie Profit

# Име на филм - текст
# Брой дни - цяло число в диапазона [1… 90]
# Брой билети  - цяло число в диапазона [100… 100000]
# Цена на билет - реално число в диапазона [5.0… 25.0]
# Процент за киното - цяло число в диапазона [5... 35]

movie_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

whole_profit = days_count * tickets_count * ticket_price
real_profit = whole_profit - (whole_profit * (cinema_percentage / 100))
print(f"The profit from the movie {movie_name} is {real_profit:.2f} lv.")
