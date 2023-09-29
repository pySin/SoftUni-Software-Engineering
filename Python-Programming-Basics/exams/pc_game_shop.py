# PC Game Shop

# Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# Име на игра - текст

number_of_games_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

x = 0
while x < number_of_games_sold:
    x += 1
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

all_sales = hearthstone + fornite + overwatch + others
hearthstone_percentages = (hearthstone / all_sales) * 100
fornite_percentages = (fornite / all_sales) * 100
overwatch_percentages = (overwatch / all_sales) * 100
others_percentages = (others / all_sales) * 100

print(f"Hearthstone - {hearthstone_percentages :.2f}%")
print(f"Fornite - {fornite_percentages :.2f}%")
print(f"Overwatch - {overwatch_percentages :.2f}%")
print(f"Others - {others_percentages :.2f}%")
