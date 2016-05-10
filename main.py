#!usr/bin/python3
"""A basic go fish game to practice my python skills again

Author: Joseph Moran
Create Date: 05/10/16"""
import random
from deck import Deck


class Game:

    def __init__(self):
        """Initialize variables"""
        self.cards = Deck()
        self.player_hand = self.cards.create_hand()
        self.ai_hand = self.cards.create_hand()
        self.deck = self.cards.deck

    def player_guess(self):
        """Allow player to guess a card"""
        player_choice = input('Guess a card')
        return player_choice

    def ai_guess(self):
        """Allow ai to guess a card"""
        ai_choice = random.sample(self.deck, 1)
        return ai_choice

    def ai_check_card(self, choice):
        """Check the persons card if the card guessed is in their hand"""
        for card in self.ai_hand:
            if choice == card:
                correct_card = card
                self.player_hand.append(correct_card)
                self.ai_hand.remove(card)
                print('You guessed correctly!')
                print('Your deck: {}'.format(self.player_hand))
        return self.player_hand, self.ai_hand

    def player__check_card(self, choice):
        """Check the persons card if the card guessed is in their hand"""
        for card in self.player_hand:
            if choice == card:
                correct_card = card
                self.ai_hand.append(correct_card)
                self.player_hand.remove(card)
        return self.player_hand, self.ai_hand

    def check_matches(self, hand):
        """Check if the person has any matches"""


game = Game()
print(game.ai_guess())
