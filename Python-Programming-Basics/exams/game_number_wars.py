# Game number Wars

# Име на първия играч - текст
# Име на втория играч - текст
# След това, до получаване на команда "End of game", се четат многократно по два реда:
# Карта, която дава първият играч- цяло число в интервала [2…9]
# Карта, която дава вторият играч -  цяло число в интервала [2…9]
# При еднакви карти на двамата играчи се прочитат нови два реда (карта,
# която дава първият и карта, която дава вторият.)

player_1_name = input()
player_2_name = input()

card_p1 = ""
card_p2 = ""

points_p1 = 0
points_p2 = 0

while True:

    card_p1 = input()
    # card_p2 = input()

    if card_p1 == "End of game":
        print(f"{player_1_name} has {points_p1} points")
        print(f"{player_2_name} has {points_p2} points")
        break
    else:
        card_p2 = input()
        card_p1 = int(card_p1)
        card_p2 = int(card_p2)

    if card_p1 == card_p2:
        p1_war_card = int(input())
        p2_war_card = int(input())
        print(f"Number wars!")

        if p1_war_card > p2_war_card:
            print(f"{player_1_name} is winner with {points_p1} points")
        elif p2_war_card > p1_war_card:
            print(f"{player_2_name} is winner with {points_p2} points")
        break
    elif card_p1 > card_p2:
        points_p1 += card_p1 - card_p2
    elif card_p2 > card_p1:
        points_p2 += card_p2 - card_p1
