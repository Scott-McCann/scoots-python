from random import randint
from random import random
def pc_Guess(Int):
    l= 1
    h = 1000
    g = randint(1,1000)
    while g != Int:
        print("is this it?: ", g)
        if g > Int:
            h = g
        elif g < Int:
            l = g + 1

        g = (l+h)//2

    print("I guessed : ", g, "YOU know I'm right!")

def GAME():
    ##http://stackoverflow.com/questions/17877870/guess-the-number-game-optimization-user-creates-number-computer-guesses?answertab=oldest#tab-top
    Int = int(input("Please enter a number between 1 and 1000(I promise I wont cheat :D):"))
    if Int < 1 or Int > 1000:
        print("[1, 1000]")
    else:
        pc_Guess(Int)


def secretmaker(int1=1, int2=1001):
    """creates a list of numbers, returns random
    """
    numbers = list(range(int1,int2))
    secret = random.choice(numbers)

    return secret

user_Guess = 0


tries = 5



print("Who should guess a number?")
game = input("(you/me) :" )
if game == "me":
    Secret = secretmaker(1,1001) #secret will be the number that must be guessed.

    print(bin(Secret))#SHHHHHHHHHH!!!!!

    print('''
    010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
    010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
    010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
    :::.    :::. ...    :::.        :   :::::::. .,:::::: :::::::..         .,-:::::/   :::.     .        :   .,::::::
     `;;;;,  `;;; ;;     ;;;;;,.    ;;;   ;;;'';;';;;;'''' ;;;;``;;;;         ,;;-''         ;;`;;      ;;,.    ;;; ;;;;''''
      [[[[[. '[[[['     [[[[[[[, ,[[[[,  [[[__[[\.[[cccc   [[[,/[[['      [[[   [[[[[[/,[[ '[[,  [[[[, ,[[[[, [[cccc
      $$$ "Y$c$$$$      $$$$$$$$$$$"$$$  $$""""Y$$$$""""   $$$$$$c        "$$c.    "$$c$$$cc$$$c $$$$$$$$"$$$ $$""""
      888    Y8888    .d888888 Y88" 888o_88o,,od8P888oo,__ 888b "88bo,     `Y8bo,,,o88o888   888,888 Y88" 888o888oo,__
      MMM     YM "YmmMMMM""MMM  M'  "MMM""YUMMMP" """"YUMMMMMMM   "W"        `'YMUP"YMMYMM   ""` MMM  M'  "MMM""""YUMMM
    010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
    010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
    010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
    ''')

    print("Hello, and welcome to Number Game! ")
    print("I am thinking of a number between 1 and 1000")
    print("Can you guess what it is?")
    print("You have 5 tries.")
    while tries > 0:
        #gives the user 5 tries, a correct guess breaks the loop. Will tell the user if the guess is "Too high" or "Too low"
        try:
            user_Guess = int(input("please enter a number: "))
            if user_Guess == Secret:
                    print("WOW!")
                    break
            elif user_Guess > Secret:
                    print("Too High")
                    tries = tries - 1
                    print("You now have " + str(tries) + " tries left.")
            elif user_Guess < Secret:
                    print("Too Low")
                    tries = tries -1
                    print("You now have " + str(tries) + " tries left.")
        except ValueError:
            print("Pretty sure I asked for a number. Enter Number: ")


    if tries > 0:
        print("CONGRATULATIONS! You win!")

    if tries == 0:
        print("GAME OVER")




###COMPUTER GUESSING GAME
if game == "you":
    print('''
 ____ ____ ____ ____ ____ ____
||i |||G |||U |||E |||S |||S ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
''')
    print("Hello! Welcome to iGUESS v.0.2.1")
    print("I will do my best to guess whatever number you enter.")
    if __name__ == GAME():
        GAME()
        #__name__ this allows the function `Game` to run.
###http://stackoverflow.com/questions/419163/what-does-if-name-main-do
