# Film Premiere

# Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
# Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
# Трети ред - брой билети - цяло число в интервала [1… 30]

movie = input()
movie_package = input()
tickets = int(input())

bill = 0

if movie == "John Wick":
    if movie_package == "Drink":
        bill = tickets * 12
    if movie_package == "Popcorn":
        bill = tickets * 15
    if movie_package == "Menu":
        bill = tickets * 19
elif movie == "Star Wars":
    if movie_package == "Drink":
        bill = tickets * 18
    elif movie_package == "Popcorn":
        bill = tickets * 25
    elif movie_package == "Menu":
        bill = tickets * 30

    if tickets >= 4:
        bill *= 1 - 0.30
elif movie == "Jumanji":
    if movie_package == "Drink":
        bill = tickets * 9
    if movie_package == "Popcorn":
        bill = tickets * 11
    if movie_package == "Menu":
        bill = tickets * 14

    if tickets == 2:
        bill *= 1 - 0.15

print(f"Your bill is {bill :.2f} leva.")
