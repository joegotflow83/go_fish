#!usr/bin/python3
"""A basic go fish game.

Author: Joseph Moran
Create Date: 05/10/16"""
import random
from deck import Deck


class Game:

    def __init__(self):
        """Initialize variables"""
        self.cards = Deck()
        self.player_hand = self.cards.create_hand()
        self.player_matches = 0
        self.ai_hand = self.cards.create_hand()
        self.ai_matches = 0
        self.deck = self.cards.deck

    def player_guess(self):
        """Allow player to guess a card"""
        player_choice = input('Guess a card ')
        return player_choice

    def ai_guess(self):
        """Allow ai to guess a card"""
        ai_choice = random.sample(self.deck, 1)
        return ai_choice

    def ai_check_card(self, choice):
        """Check the ai's card if the card guessed is in their hand"""
        for card in self.ai_hand:
            if choice == card:
                self.player_hand.append(card)
                self.ai_hand.remove(card)
        return self.player_hand, self.ai_hand

    def player_check_card(self, choice):
        """Check the players card if the card guessed is in their hand"""
        for card in self.player_hand:
            if choice == card:
                self.ai_hand.append(card)
                self.player_hand.remove(card)
        return self.player_hand, self.ai_hand

    def add_player_match(self):
        """Add a match to the players score"""
        return self.player_matches + 1

    def add_ai_match(self):
        """Add a match to the ai score"""
        return self.ai_matches + 1

    def which_player(self, hand, card, next_card):
        """Determine which persons hand is evaluated"""
        if hand == self.player_hand:
            print('You have a suit! The two cards are {} and {}.'.format(card, next_card))
            self.add_player_match()
        else:
            print('The ai has a suit! The two cards are {} and {}.'.format(card, next_card))
            self.add_ai_match()

    def check_suit(self, hand):
        """Check if the person has any suits"""
        sorted_hand = sorted(hand)
        for index, card in enumerate(sorted_hand):
            try:
                next_card = sorted_hand[index + 1]
            except IndexError:
                continue
            if card[0] == next_card[0]:
                self.which_player(hand, card, next_card)
                hand.remove(card)
                hand.remove(next_card)
        return hand

    def play(self):
        """Play the game"""
        while self.player_matches < 3 or self.ai_matches < 3:
            player_guess = self.player_guess()
            self.ai_check_card(player_guess)
            self.check_suit(self.player_hand)
            ai_guess = self.ai_guess()
            self.player_check_card(ai_guess)
            self.check_suit(self.ai_hand)
        return 'Thanks for playing!'


game = Game()
print("Welcome to Go Fish! Try to beat the ai!")
print("Here is your deck \n {}\n".format(game.player_hand))
print(game.play())
