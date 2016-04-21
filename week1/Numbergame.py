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

Secret = secretmaker(1,1001) #secret will be the number that must be guessed.
tries = 5
print(Secret)
print("Hello and welcome to Number Game! ")

while tries > 0:
    #gives the user 5 tries, a correct guess breaks the loop. 
        try:
            user_Guess = int(input("please enter a number: "))
            if user_Guess == Secret:
                print("WOW!")
                break
            if user_Guess != Secret:
                print("WRONG!")
                tries = tries - 1
        except ValueError:
            print("Pretty sure I asked for a number. Enter Number: ")

if tries > 0:
    print("CONGRATULATIONS! You win!")

if tries == 0:
    print("GAME OVER")
