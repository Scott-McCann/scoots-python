import random
print(Welcome to PYMAN)
print("Do you want to play a game? ")

def userGuess(guessList):
    while True:
        """asks the user for a letter, checks if that letter is already in the guesslist, checks for correct input.
        """
        print("Please guess a letter: " )
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("please enter a single letter.")
        elif guess in guessList:
            print("You already guessed that letter!")
        elif guess.isdigit():
            print(Please enter a letter.)
        else:
            return guess

def playAgain():
    """ simply asks the user if they would like to play the game again.
    """
    print("Do you want to play again?")
    return input().lower().startswith('y')

def getWord
    """picks a random word,
    wordlist = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            wordlist.append(line.strip())
            secretWord = choice(wordlist)
            wLength = len(secretWord)





tries = 5
guesses = 0
hint = wLength * [" "]
correctLetters = 0
wrongLetters = 0
userletters = ""
while wrongLetters != tries and

print(secretWord)
print(wLength)
