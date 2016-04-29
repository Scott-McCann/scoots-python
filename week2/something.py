import random

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14] *4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = 'J'
        if card == 12:card = 'Q'
        if card == 13:card = 'K'
        if card == 14:card = 'A'
        hand.append(card)
    return hand

def play_again():
    again = input("Play again? (y/n) : ").lower()
    if again == 'y':
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        game()
    else:
        print("BYE!")


def total(hand):
    total = 0
    for card in hand:
        if card == "jack" or card == "queen" or card  == "king":
            total += 10
        elif card == "ace":
            if total >= 11:
                total +=1
            else:
                total += 11

        else: total += card

    return total

def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"

def print_hands(dealer_hand, player_hand):

    print("the dealer has " + str(dealer_hand) + "for a total of " + str(total(dealer_hand)))
    print("You have " + str(player_hand) + "for a total of " + str(total(dealer_hand)))



def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_hands(dealer_hand, player_hand)
        print("YOU WIN!")

    elif total(dealer_hand) == 21:
        print("YOU LOSE!")

    elif total(player_hand) > 21:
        print_hands(dealer_hand, player_hand)
        print("Sorry You Busted")

    elif total(dealer_hand) > 21:
        print_hands(dealer_hand, player_hand)
        print("Deler busts! You win!")

    elif total(player_hand) < total(dealer_hand):
        print_hands(dealer_hand, player_hand)
        print("Dealer Wins. YOU LOSE!")

    elif total(player_hand) > total(dealer_hand):
        print_hands(dealer_hand, player_hand)
        print("YOU WIN!")


def game():
    choice = 0
    print('welcome to PYJACK')
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != 'q':
        print("The dealer is showing a " + str(dealer_hand))
        print("you have a " + str(player_hand) + "for a total of " + str(total(player_hand)))

        choice = input("do you want to [H]it, [S]tand, or [Q]: ").lower()

        if choice == 'h':
            hit(player_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == 's':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand)
            play_again()
        elif choice == "q":
            print("SEE YA!")
            break

if __name__ == "__main__":
    game()
