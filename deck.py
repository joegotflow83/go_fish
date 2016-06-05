import itertools
import random


class Deck:

    def __init__(self):
        self.suit = 'chsd'
        self.rank = '23456789TJQKA'
        self.deck = tuple([''.join(card) for card in itertools.product(self.rank, self.suit)])
        self.hand = random.sample(self.deck, 7)

    def create_hand(self):
        return self.hand

    def print_deck(self):
        for card in self.deck:
            print(card)


deck = Deck()
