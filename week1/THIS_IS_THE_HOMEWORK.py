#Asks for a name, favorite color, and age.
#Asks the user if they want to continue adding people.
#If so, repeats from step #1
#If not, prints out the information received like so: Name: <> Color: <> Age: <> --- [next person]
people = {}
while True:
    name = input("Enter full name: ")
    if len(name) == 0:
        name = input("Please enter a Name: ")
        if len(name) == 0:
            name = input("Now your just being Difficult. Enter Name: ")
            if len(name) == 0:
                name = input("This is a fun game. Enter Name: ")
                if len(name) == 0:
                    name = input("I know where you live... Enter Name: ")
    color = input("Favorite Color?: ")
    if len(color) == 0:
        color = input("Please Enter a Color")
        if len(color) == 0:
            name = input("are you serious? Enter a Color: ")
            if len(color) == 0:
                name = input("I see... Enter a Color: ")
                if len(color) == 0:
                    name = input("You must have been reeeally popular in school. Enter Color: ")
    age = input("Enter age: ")
    if len(age) == 0:
        age = input("Please enter your age: ")
        if len(age) == 0:
            age = input("STAHP! Enter Age: ")
            if len(age) == 0:
                age = input("Why are you like this? Enter Age: ")
                if len(age) == 0:
                    age = input("Did mommy and daddy not love you enough? Enter Age: ")
    cont = input("Would you like to continue (y)(n): ")
    if cont == 'n':
        break
    people[name]= {'color': color, 'age': age}

print(people)
