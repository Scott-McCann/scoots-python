cont='y'
#will be used to control while loop
piglist=[]
#will be used for `for` loop at the end.
vow = ('a', 'e', 'i', 'o', 'u')
def convert_word(word):
    first = word[0]                                          #first = the first letter of (word)
    if first in vow:                                         #checks if first is a part of the 'vow' dataset
        return word[1:] + "say"                              # drops the first letter and adds "say"
    else:
        return word[1:] + word[0] + "ay"                     #Removes first letter of word, adds first letter of word to the end, adds "ay"

def convert_sentence(sentence):
    wordsList = sentence.split(' ')                          #splits the argument into a list
    pigSentence = ""
    for word in wordsList:                                   #converts each word returns translated sentence.
        pigSentence = pigSentence + convert_word(word)
        pigSentence = pigSentence + " "                     #IMPORTANT! adds spacing.
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

print("I'm not very powerful yet. One day I will be a fully grown PYPIGGY")
print("Until then, however, I can only handle sentences that are all lowercase with no punctuation")
print("OINK!")
while cont is 'y':



    normal= input("please enter a sentence: ")

    cont= input("continue?: ")

    if cont is "n":
             continue
print('''
  &,----.,_       &,----.,_       &,----.,_       &,----.,_
  /      ' "_     /      ' "_     /      ' "_     /      ' "_
 ,_ )___(&,--=-.,_(  )__&,---=.,_ (  )_&,----:,_  (  )&,----.;_
 ' "_```}/      ' "_/ ``/      ' "_}/ `/      ' "_ }/ /      ' "_
_( ,_@  "(  )___( ,_@   (  )___( ,_@"  (  )___( ,_@"" (  )___( ,_@
` &,----.,_/````&,----.,_ /```&,----.,_ }/``&,----.,_  }/`&,----.,_
  /      ' "_   /      ' "_   /      ' "_"  /      ' "_"" /      ' "_
  (  )___( ._@  (  )___( ._@  (  )___( ._@  (  )___( ._@  (  )___( ._@
   }/%   }{      }/%   }{      }/%   }{      }/%   }{      }/%   }{
,_""  &,----.,_ "" &,----.,_  ""&,----.,_   "&,----.,_    &,----.,_
 ' "_  /      ' "_  /      ' "_  /      ' "_  /      ' "_  /      ' "_
_( ,_@ (  )___( ,_@ (  )___( ,_@ (  )___( ,_@ (  )___( ,_@ (  )___( ,_@
`}{     }/````}{     }/````}{     }/````}{     }/````}{     }/````}{
 ""     ""    ""     ""    ""     ""    ""     ""    ""     ""    ""
''')
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
