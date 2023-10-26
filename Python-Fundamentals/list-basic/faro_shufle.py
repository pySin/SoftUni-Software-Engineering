# Faro Shuffle

initial_deck_cards = input().split()
number_of_shuffles = int(input())

inner_deck = initial_deck_cards[1:-1]

for i in range(number_of_shuffles):
    first_half = inner_deck[:len(inner_deck) // 2]
    second_half = inner_deck[(len(inner_deck) // 2):]
    inner_deck = []
    for j in range(len(first_half)):
        inner_deck.append(second_half[j])
        inner_deck.append(first_half[j])

final_deck = [initial_deck_cards[0]] + inner_deck + [initial_deck_cards[-1]]
print(final_deck)
