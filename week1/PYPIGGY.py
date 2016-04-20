cont='y'
piglist=[]
vow = ('a', 'e', 'i', 'o', 'u')
def convert_word(word):
    first = word[0]
    if first in vow:
        return word[1:] + "say"
    else:
        return word[1:] + word[0] + "ay"

def convert_sentence(sentence):
    wordsList = sentence.split(' ')
    pigSentence = ""
    for word in wordsList:
        pigSentence = pigSentence + convert_word(word)
        pigSentence = pigSentence + " "
    return pigSentence

print("Hello and welcome to PYPIGGY v0.9.0")
print(
  '''
          ""',_`""\        .---,
            \   :-""``/`    |
             `;'     //`\   /
             /   __     |   ('.
            |_ ./O)\     \  `) |
           _/-.    `      `"`  |`-.
       .-=; `                  /   `-.
      /o o \   ,_,           .        '.
      L._._;_.-'           .            `'-.
        `'-.`             '                 `'-.
            `.         '                        `-._
              '-._. -'                              '.
                 \                                    `|
                  |                                     |
                  |    |                                 ;   _.
                  \    |           |                     |-.((
                   ;.  \           /    /                |-.`\)
                   | '. ;         /    |                 |(_) )
                   |   \ \       /`    |                 ;'--'
                    \   '.\    /`      |                /
                     |   /`|  ;        \               /
                     |  |  |  |-._      '.           .'
                     /  |  |  |__.`'---"_;'-.     .-'
                    //__/  /  |    .-'``     _.-'`
                          //__/   //___.--''`
''')
while cont is 'y':



    normal= input("please enter a sentence: ")

    cont= input("continue?: ")

    if cont is "n":
             continue
print(convert_sentence(normal))


























#     aword= input("please enter a word: ")
#     if aword[0] == 'a':
#         newword = aword[1:]+ aword[0]+ "say"
#     elif aword[0] == 'e':
#         newword = aword[1:]+ aword[0]+ "say"
#     elif aword[0] == 'i':
#         newword = aword[1:]+ aword[0]+ "say"
#     elif aword[0] == 'o':
#         newword = aword[1:]+ aword[0]+ "say"
#     elif aword[0]== 'u':
#         newword = aword[1:]+ aword[0]+ "say"
#     else:
#         newword = aword[1:]+ aword[0] +"ay"
#
#
#
#     piglist.append(newword)
#     cont= input("continue?: ")
#     if cont is "n":
#         continue
# for pig in (piglist):
#         print(pig)
