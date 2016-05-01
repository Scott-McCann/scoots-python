from random import shuffle
import time
import os
import sys

class blackjack():
    def __init__(self, player_names, number_of_decks, wallet=100):
        self.how_many_players = len(player_names)
        self.number_of_decks = number_of_decks
        self.wallet = wallet
        self.running = True
        self.deck = []
        self.players = []
        self.dealer_hand = []
        self.dealer_total = 0
        self.shuffle_deck()
        shuffle(self.deck)
        self.get_player_name(player_names)
        self.build_players_interactive()

    def get_Deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for card in cards:
    	         self.deck.append(card+' of '+suit)

    def show_hand(self, hand):
        print('''-----------YOUR CARDS---------------''')
        print('Cards in hand: ', end=' ')
        for card in hand:
            print(card, end=', ')
        print()

    def show_dealer_hand(self, hand):
        print('''-----------Dealer's Cards---------''')
        print('Cards in hand: ', end=' ')
        for card in hand:
            print(card, end=', ')
        print()


    def deal_card(self):
        try:
            return self.deck.pop()
        except:
            print("Out of cards. Reshuffling.")
            self.shuffle_deck()
            return self.deck.pop()

    def value_hand(self, hand):
        value = 0
        aces = 0
        for card in hand:
            try:
                value += int(card.split(' ')[0])
            except:
                    if('A' == card[0]):
                        value += 1
                        aces += 1
                    else:
                        value += 10
        while(aces):
            if(21 >= value + 10):
                aces -= 1
                value += 10
            if(21 < value + 10):
                break
        return value


    def deal_cards(self):
        for player in self.players:
            player['hand'] = [self.deal_card(), self.deal_card()]


    def take_Bets(self):
        for player in self.players:
            choice = 'h'
            print("________________ {}'s turn._____________________".format(player['name']))
            print('________________You have {}.____________________'.format(player['Wallet']))
            try:
            	player['Bet'] = int(input('''How much would you like to bet? :
                $'''))
            except:
            	player['Bet'] = 10
            if (player['Bet'] > player['Wallet']):
            	player['Bet'] = player['Wallet']
            if (10 > player['Bet']):
            	player['Bet'] = 10

            self.show_hand(player['hand'])

            while(('h' == choice)) :
                player['value'] = self.value_hand(player['hand'])
                if( 21 < player['value'] ):
                    print("BUST: {} went over 21.".format(player['name']))
                    player['value'] = -1
                    break

                print("{}'s hand has a value of {}.".format(player['name'], player['value']))
                choice = input('Hit or Stay? [h/s] ')
                if('h' == choice):
                    card = self.deal_card()
                    print("Got a {}.".format(card))
                    player['hand'].append(card)



    def dealer_turn(self):

        self.dealer_hand = [self.deal_card(), self.deal_card()]
        print("Dealers Turn.")
        self.show_dealer_hand(self.dealer_hand)
        while(17 > self.value_hand(self.dealer_hand)):
            print("Dealer hits...")

            print('.')
            time.sleep(1)
            print('..')
            time.sleep(1)

            card = self.deal_card()
            print("Dealer got a {}.".format(card));
            self.dealer_hand.append(card)
        print("Dealer Stays....")
        self.dealer_total = self.value_hand(self.dealer_hand)
        self.show_dealer_hand(self.dealer_hand)
        print("Dealer's {}.".format(self.dealer_total))
        if(21 < self.dealer_total):
            print("Dealer went bust!")
            self.dealer_total = -1

    def who_wins(self):
        """ Check if players beat dealer """
        for player in reversed(self.players):
            if((player['value'] > self.dealer_total) & (1 < player['value'])):
                print("CONGRATUALTIONS {} You Win!".format(player['name']))
                player['Wallet'] += player['Bet']
                player['Bet'] = 0
            elif((self.dealer_total > player['value']) & (1 < self.dealer_total)):
                print("Dealer beat {}".format(player['name']))
                player['Wallet'] -= player['Bet']
                player['Bet'] = 0
            else:
                print("{} PUSH: Its a draw!".format(player['name']));
                player['Bet'] = 0
            if(1 > player['Wallet']):
                print("{} is out of the game!".format(player['name']));
                self.players.remove(player)
                self.how_many_players -= 1
                if (1 > self.how_many_players):
                    self.running = False
                    return

    def shuffle_deck(self):
        if len(self.deck) < 11:
            for _ in range(self.number_of_decks):
                self.get_Deck()

    def get_player_name(self, player_names):
        for name in player_names:
            self.players.append({'name': name, 'hand': [], 'value': 0, 'Wallet': self.wallet, 'Bet': 0})

    def build_players_interactive(self):
        for i in range(self.how_many_players):
            name = input('Next Player name: ')
            self.players.append({'name': name, 'hand': [], 'score': 0, 'Wallet': self.wallet, 'bet': 0})



def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def play_again():
    again = input("Play again? (y/n) : ").lower()
    choice = None
    if again == 'y':
        cls()
    else:
        cls()
        sys.exit()

def main():
    cls()
    print('''
MM"""""""`YM M""MMMM""M MMMMMMMM""M MMP"""""""MM MM'""""'YMM M""MMMMM""M
MM  mmmmm  M M. `MM' .M MMMMMMMM  M M' .mmmm  MM M' .mmm. `M M  MMMM' .M
M'        .M MM.    .MM MMMMMMMM  M M         `M M  MMMMMooM M       .MM
MM  MMMMMMMM MMMb  dMMM MMMMMMMM  M M  MMMMM  MM M  MMMMMMMM M  MMMb. YM
MM  MMMMMMMM MMMM  MMMM M. `MMM' .M M  MMMMM  MM M. `MMM' .M M  MMMMb  M
MM  MMMMMMMM MMMM  MMMM MM.     .MM M  MMMMM  MM MM.     .dM M  MMMMM  M
MMMMMMMMMMMM MMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM
                - A BlackJack Game-

                   HELLO! Welcome to PYJACK!
               -                               -
                 try to get 21 without going over.
                 -       or at least beat the dealer    -
                 ''')
    try:
        number_of_decks = int(input('How many decks? '))
    except:
        print("Starting with 4.")
    number_of_decks = 4
    name = 'a'
    player_names = []
    while (True):
        name = input('Whats your name? : ')
        if('' == name):
            break
        player_names.append(name)
        game = blackjack(player_names, number_of_decks)
        while (game.running):
            game.deal_cards()
            game.take_Bets()
            game.dealer_turn()
            game.who_wins()
            play_again()



if "__main__" == __name__:
	main()
