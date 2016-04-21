import random
def pc_Guess(int1=1,int2=1000):
    """return a random integer from between two integers
    default values:(int1 = 1, int2 = 2)
    """
    return random.randint(int1,int2)


def secretmaker(int1=1, int2=1001):
    """creates a list of numbers, returns random
    """
    numbers = list(range(int1,int2))
    secret = random.choice(numbers)

    return secret

user_Guess = 0
Secret = secretmaker(1,1001) #secret will be the number that must be guessed.
tries = 5
print(bin(Secret))
print('''
010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
010011100111010101101101 011000100110010101110010 01000111010000010100110101000101 01000111010000010100110101000101
:::.    :::. ...    :::.        :   :::::::. .,:::::: :::::::..         .,-:::::/   :::.     .        :  .,::::::
 `;;;;,  `;;; ;;     ;;;;;,.    ;;;   ;;;'';;';;;;'''' ;;;;``;;;;      ,;;-''        ;;`;;    ;;,.    ;;; ;;;;''''
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
print("can you guess what it is?")
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
        elif user_Guess < Secret:
                print("Too Low")
                tries = tries -1
    except ValueError:
        print("Pretty sure I asked for a number. Enter Number: ")


if tries > 0:
    print("CONGRATULATIONS! You win!")

if tries == 0:
    print("GAME OVER")
