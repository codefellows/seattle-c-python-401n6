# Warm-Up Exercise

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
card_names = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Feature Tasks
# - Use the data from above:
#   DONE: Create a Card Class with a suit and "value" attribute.


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'
#   DONE: Create a Deck Class


class Deck:
    # DONE Instantiate all 52 cards and add them to a list
    def __init__(self):
        self.deck = []
        self.dealt = []
        for suit in suits:
            for card in card_names:
                self.deck.append(Card(suit, card))

    def __str__(self):
        return f'{[value for value in self.deck if print(value)]}'
#     DONE: Deal a single card from the deck

    def deal(self):
        single_card = self.deck.pop(random.randrange(len(self.deck)))
        self.dealt.append(single_card)
        return single_card


if __name__ == '__main__':
    deck = Deck()
    # print(deck)
    # card = Card('Hearts', 'two')
    # print(card)
    print(deck.deal())
