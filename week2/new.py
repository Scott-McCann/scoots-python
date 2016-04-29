import unittest
import random

class PlayingCard:
    def __init__(self, value, suit):
        if suit not in self.suits:
            raise AttributeError("suit not valid")
        if value not in self.values:
            raise AttributeError("value not valid")

        self.value = value
        self.suit = suit

    suits = ('hearts', 'clubs', 'diamonds', 'spades')
    values = {'ace': 'ace',
              '2': 'duece',
              '3': 'three',
              '4': 'four',
              '5': 'five',
              '6': 'six',
              '7': 'seven',
              '8': 'eight',
              '9': 'nine',
              '10': 'ten',
              'jack': 'jack',
              'queen': 'queen',
              'king': 'king'}

    def shortName(self):
        return '{0}{1}'.format(self.value[0].upper(),
                               self.suit[0].upper())

    def longName(self):
        return '{0} of {1}'.format(self.values[self.value],
                                   self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in PlayingCard.suits:
            for value in PlayingCard.values:
                self.cards.append(PlayingCard(value, suit))


    def shuffle(self):
        random.shuffle(self.cards)

        return




class TestPlayingCard(unittest.TestCase):
    def testSuits(self):
        self.assertEqual(4, len(PlayingCard.suits))
        self.assertTrue('hearts' in PlayingCard.suits)
        self.assertFalse('weasels' in PlayingCard.suits)

    def testValues(self):
        self.assertEqual(13, len(PlayingCard.values))
        self.assertTrue('9' in PlayingCard.values)
        self.assertTrue('21' not in PlayingCard.values)

    def testInit(self):
        pc1 = PlayingCard('ace', 'hearts')
        self.assertEqual('ace', pc1.value)
        self.assertEqual('hearts', pc1.suit)
        with self.assertRaises(TypeError):
            pc2 = PlayingCard()

        with self.assertRaises(AttributeError):
            pc3 = PlayingCard('duke', 'earl')

    def testShortName(self):
        pc1 = PlayingCard('9', 'clubs')
        self.assertEqual('9C', pc1.shortName())

    def testLongName(self):
        pc = PlayingCard('10', 'hearts')
        self.assertEqual('ten of hearts', pc.longName())

class TestDeck(unittest.TestCase):
    def testInit(self):
        deck = Deck()
        self.assertEqual(52, len(deck.cards))

    def testShuffle(self):
        deck = Deck()
        copy_of_cards = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(copy_of_cards, deck.cards)

def game_loop():
    pass
    # Or do game logic in a function

if __name__ == '__main__':
    # Game loop goes here
    # or call game_loop()
    cont = 'y'
    while 'y' in cont.lower():
        deck = Deck()
        deck.shuffle()
        playercards = [deck.cards.pop(), deck.cards.pop()]
        for len(playercards) print
# TO run tests from the commandline:
# Be in the same directory as this filename
# $ python3 -m unittest blackjack

## TO Use these classes in iPython:
# 1. run 'ipython3' *in the same directory as this file*
# Syntax is:
#  from <filename without .py> import <name of class>:
# from blackjack import PlayingCard
# PlayingCard.suits
# Out[2]: ('hearts', 'clubs', 'diamonds', 'spades')
