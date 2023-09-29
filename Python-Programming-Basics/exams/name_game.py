# Name Game

# Име на играча с дължина n - текст
# За всеки играч се четат n на брой реда:
# число – цяло число в интервала[0…127]

winner_name = ""
top_score = 0

while True:

    player_name = input()
    player_score = 0

    if player_name == "Stop":
        print(f"The winner is {winner_name} with {top_score} points!")
        break

    for letter in player_name:
        ascii_number = int(input())
        if ascii_number == ord(letter):
            player_score += 10
        else:
            player_score += 2

    if player_score >= top_score:
        winner_name = player_name
        top_score = player_score


