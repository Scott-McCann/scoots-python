myName = input("Enter your name: ")

print("hello, " + myName)

myAge = None
try:
    myAge = int(input("How old are you, " + myName + "? "))
except:
    print("I don't understand you")

if myAge:
    print("Maybe you were born in " + str(2016 - myAge))

    
