# Easter trip

# Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
# Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23",
# "24-27" или "28-31"
# Трети ред - брой нощувки - цяло число в интервала [1… 100]

destination = input()
dates = input()
nights = int(input())

bill = 0

if destination == "France":
    if dates == "21-23":
        bill = nights * 30
    if dates == "24-27":
        bill = nights * 35
    if dates == "28-31":
        bill = nights * 40

if destination == "Italy":
    if dates == "21-23":
        bill = nights * 28
    if dates == "24-27":
        bill = nights * 32
    if dates == "28-31":
        bill = nights * 39
if destination == "Germany":
    if dates == "21-23":
        bill = nights * 32
    if dates == "24-27":
        bill = nights * 37
    if dates == "28-31":
        bill = nights * 43

print(f"Easter trip to {destination} : {bill :.2f} leva.")
