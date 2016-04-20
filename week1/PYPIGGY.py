cont='y'
piglist=[]
while cont is 'y':
    print("Hello and welcome to PYPIGGY v0.0.2")
    aword= input("please enter a word: ")
    newword = aword[1:]+ aword[0] +"ay"
    piglist.append(newword)
    cont= input("continue?: ")
    if cont is "n":
        break
print(piglist)
