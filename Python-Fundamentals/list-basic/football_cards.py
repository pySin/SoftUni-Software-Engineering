# Football Cards

cards_sequence = input()

team_A_cards = 11
team_B_cards = 11

cards_list = set(cards_sequence.split())

for card in cards_list:
    if "A" in card:
        team_A_cards -= 1
    elif "B" in card:
        team_B_cards -= 1

    if team_B_cards < 7 or team_A_cards < 7:
        break


print(f"Team A - {team_A_cards}; Team B - {team_B_cards}")
if team_B_cards < 7 or team_A_cards < 7:
    print("Game was terminated")
