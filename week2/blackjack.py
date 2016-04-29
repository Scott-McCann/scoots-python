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
              '2': 'two',
              '3': 'three',
              '4': 'four',
              '5': 'five',
              '6': 'six',
              '7': 'seven',
              '8': 'eight',
              '9': 'nine',
              '10': 'ten',
              'queen': 'queen',
              'king': 'king',
              'jack': 'jack'}

    def short_name(self):
        """Returns the Short Name of a card ex.(KH,7S)"""
        return '{0}{1}'.format(self.value[0].upper(),
                               self.suit[0].upper())


    def long_name(self):
        """Returns long Name of card ex(King of Hearts , Seven of Spades)"""
        return '{0} of {1}'.format(self.values[self.value].capitalize(),
                                   self.suit.capitalize())

    def Rank(self):
        if self.value in ('jack', 'queen', 'king'):
            return 10
        elif self.value == 'ace':
            return 11
        else:
            return int(self.value)


class Deck():
    def __init__(self):
        self.cards = []
        for suit in PlayingCard.suits:
            for value in PlayingCard.values:
                self.cards.append(PlayingCard(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def deal_card(self):
        return self.cards.pop()


class Hand():
    def __init__(self):
        self.cards = []


    def get_card(self, aCard):
        return self.cards.append(aCard)


    def get_hand(self):
        for num in range(0, len(self.cards)-1):
            print(self.cards[num].long_name())


    def get_Sum(self):
        cardTotal = 0
        for num in range(0, len(self.cards)-1):
            cardTotal += self.cards[num].Rank()
        return cardTotal


    def get_results(self):
        self.get_hand()
        print('Card Total: {0}'.format(self.get_Sum()))


    def hit(self):
        self.cards.pop()




def play_again():
    again = input("Play again? (y/n) : ").lower()
    if again == 'y':
        dealerhand = []
        playerhand = []
        deck = Deck()
        deck.shuffle
        game()
    else:
        print("BYE!")

if __name__ == '__main__':


    deck = Deck()
    deck.shuffle()
    playerHand = Hand()
    dealerHand = Hand()
    choice = 'h'

    for card in range(3):
        playerHand.get_card(deck.deal_card())
        dealerHand.get_card(deck.deal_card())


    if choice != 'q':
        print('YOUR HAND')
        playerHand.get_results()
        print('''########################################################
                 ########################################################''')
        print('')
        print('')
        print("DEALER'S HAND")
        dealerHand.get_results()

        choice = input("do you want to [H]it, [S]tand, or [Q]: ").lower()

        while dealerHand.get_Sum() < 17:
            dealerHand.get_card(Hand)

        print('YOUR HAND')
        playerHand.get_results()
        print('''##########################################################
                 ##########################################################''')
        print("DEALER'S HAND")
        dealerHand.get_results()


    #     print('Your hand: ']
    #     playerHand.get_results()
    #     dealerHand.get_results()
    # elif choice == 's':
    #     while dealerHand.get_Sum() < 17:
    #         dealerHand.get_card(deck.deal_card())
    #     dealerHand.get_Sum()
    #     play_again()
    # elif choice == "q":
    #     print("SEE YA!")
