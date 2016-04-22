import random
print(Welcome to PYMAN)
print("Do you want to play a game? "

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
