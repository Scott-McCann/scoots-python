cont='y'
piglist=[]
vow = ('a', 'e', 'i', 'o', 'u')
def convert_word(word):
    first = word[0]
    if first in vow:
        return word[1:] + "say"
    else:
        return word[1:] + word[0] + "ay"


print("Hello and welcome to PYPIGGY v0.0.2")
while cont is 'y':



    aword= input("please enter a word: ")
    pig= convert_word(aword)
    piglist.append(pig)

    cont= input("continue?: ")

    if cont is "n":
             continue

for piggy in piglist:
    print(piggy)


























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
