# Deck of Cards


deck_of_cards = []


class Card:

    superior_cards = {
        "A": 11,
        "J": 12,
        "D": 13,
        "K": 14
    }

    def __init__(self, symbol, suit: str):
        self.symbol = symbol
        self.suit = suit

    @property
    def power(self):
        if isinstance(self.symbol, int):
            return int(self.symbol)
        else:
            return Card.superior_cards[self.symbol]


card_ideas = [[2, "Spade"], [2, "Hearts"], [2, "Diamonds"], [2, "Clubs"],
              [3, "Spade"], [3, "Hearts"], [3, "Diamonds"], [3, "Clubs"],
              [4, "Spade"], [4, "Hearts"], [4, "Diamonds"], [4, "Clubs"],
              [5, "Spade"], [5, "Hearts"], [5, "Diamonds"], [5, "Clubs"],
              [6, "Spade"], [6, "Hearts"], [6, "Diamonds"], [6, "Clubs"],
              [7, "Spade"], [7, "Hearts"], [7, "Diamonds"], [7, "Clubs"],
              [8, "Spade"], [8, "Hearts"], [8, "Diamonds"], [8, "Clubs"],
              [9, "Spade"], [9, "Hearts"], [9, "Diamonds"], [9, "Clubs"],
              [10, "Spade"], [10, "Hearts"], [10, "Diamonds"], [10, "Clubs"],
              ["A", "Spade"], ["A", "Hearts"], ["A", "Diamonds"], ["A", "Clubs"],
              ["J", "Spade"], ["J", "Hearts"], ["J", "Diamonds"], ["J", "Clubs"],
              ["D", "Spade"], ["D", "Hearts"], ["D", "Diamonds"], ["D", "Clubs"],
              ["K", "Spade"], ["K", "Hearts"], ["K", "Diamonds"], ["K", "Clubs"]
              ]

for i in range(len(card_ideas)):
    deck_of_cards.append(Card(card_ideas[i][0], card_ideas[i][1]))

print(deck_of_cards)

print(f"Symbol: {deck_of_cards[40].symbol}")
print(f"Suit: {deck_of_cards[40].suit}")
print(f"Power: {deck_of_cards[40].power}")
