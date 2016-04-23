import random
from random import choice

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
            print("Please enter a letter.")
        else:
            return guess

def playAgain():
    """ simply asks the user if they would like to play the game again.
    """
    print("Do you want to play again?")
    return input().lower().startswith('y')

def getWord():
    """picks a random word
    """
    wordlist = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            wordlist.append(line.strip())
            secretWord = choice(wordlist)

        return secretWord



def blank(missed, correct, secretWord):
    print("Missed letters:", end = '')
    for letter in missed:
        print(letter)
    print()

    blanks = '_' * len(secretWord)

    for alpha in range(len(secretWord)):
        if secretWord[alpha] in correct:
            blanks = blanks[:alpha] + secretWord[alpha] + blanks [alpha+1:]

    for letter in blanks:
        print(letter, end = '')
    print()

wordList = []
missed = ''
correct = ''
secretWord = getWord()
wLength = len(secretWord)
gameOver = False

print("Welcome to PYMAN")
print("Do you want to play a game? ")
print(secretWord)

while gameOver == False:
    blank(missed, correct, secretWord)

    guess = userGuess(missed + correct)

    if guess in secretWord:
        correct = correct + guess
