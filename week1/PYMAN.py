import random
from random import choice
#for some reason choice wouldn't import implicity


def user_guess(guessList):
    while True:
        """asks the user for a letter, checks if that letter is already in the
           guesslist, checks for correct input.
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


def play_again():
    """asks the user if they would like to play the game again."""

    print("Do you want to play again?")
    return input().lower().startswith('y')


def get_word():
    """picks a random word"""

    wordlist = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            wordlist.append(line.strip())
            secretWord = choice(wordlist)

        return secretWord



def blank(missed, correct, secretWord):
    """prints out an amount of blanks equal to the secretWord"""
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




tries = 8
wordList = []
missed = ''
correct = ''
secretWord = get_word()
wordLength = len(secretWord)
gameOver = False

print("Welcome to PYMAN")
print("Do you want to play a game? ")
print(secretWord)

#Game begins here.
while gameOver is False :
    blank(missed, correct, secretWord)
    print("There are " + str(wordLength) + " Letters!")
    guess = user_guess(missed + correct)

    #Will check if the Users guess is in the word.
    if guess in secretWord:
        correct = correct + guess

        #Checks if letter is in the word.
        allCorrect = True
        for alpha in range(len(secretWord)):
            if secretWord[alpha] not in correct:
                allCorrect = False
                break

        #Win Condition
        if allCorrect:
            print("Thats Right! The word is "
            + secretWord
            + "! You Win! :D")
            gameOver = True

    #adds missed letters to list, counts down tries.
    else:
        missed = missed + guess
        tries = tries - 1
        print("You now have : " + str(tries))

        #Loss Condition
        if tries == 0:
            print("You have lost")
            print("The secret word is : " + secretWord)
            gameOver = True


    if gameOver:
        if play_again():
            missed = ""
            correct = ""
            gameOver = False
            secretWord = get_word()
        else:
           break
