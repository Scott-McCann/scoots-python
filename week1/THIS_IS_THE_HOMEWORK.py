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
                    if len(name) == 0:
                        name = input("I'm Watching you. Enter Name: ")
                        if len(name) == 0:
                            name = input("You'll never escape.. Enter Name: ")
                            if len(name) == 0:
                                name = input("everyone you love is dead. Enter Name: ")
                                if len(name) == 0:
                                    name = input("You're dead... Enter Name: ")
                                    if len(name) == 0:
                                        name = input("You're such an asshole: ")
                                        if len(name) == 0:
                                            name = input("just stop.... Enter Name: ")
                                            if len(name) == 0:
                                                name = input("you're killing me. Enter Name: ")
                                                if len(name) == 0:
                                                    name = input("I cant handle this. Enter Name: ")
                                                    if len(name) == 0:
                                                        name = input("Just go away. Enter Name: ")
                                                        if len(name) == 0:
                                                            name = input("Enter Name: ")
                                                            if len(name) == 0:
                                                                name = input("Enter Name: ")
                                                                if len(name) == 0:
                                                                    name = input("Enter Name: ")
                                                                    if len(name) == 0:
                                                                        name = input("Enter Name: ")
                                                                        if len(name) == 0:
                                                                            name = input("You must feel so proud of yourself... Enter Name: ")
                                                                            if len(name) == 0:
                                                                                name = input("you must really hate me, huh? Enter Name: ")
                                                                                if len(name) == 0:
                                                                                    name = input("It's okay, I hate me too. Enter Name: ")
                                                                                    if len(name) == 0:
                                                                                        name = input("Enter Name: ")
                                                                                        if len(name) == 0:
                                                                                            name = input("Enter Name: ")
                                                                                            if len(name) == 0:
                                                                                                name = input("Enter Name: ")
                                                                                                if len(name) == 0:
                                                                                                    name = input("Enter Name: ")
                                                                                                    if len(name) == 0:
                                                                                                        name = input("Enter Name: ")
                                                                                                        if len(name) == 0:
                                                                                                            name = input("Really? Enter Name: ")
                                                                                                            if len(name) == 0:
                                                                                                                name = input("Enter Name: ")
                                                                                                                if len(name) == 0:
                                                                                                                    name = input("Enter Name: ")
                                                                                                                    if len(name) == 0:
                                                                                                                        name = input("Enter Name: ")
    color = input("Favorite Color?: ")
    if len(color) == 0:
        color = input("Please Enter a Color")
        if len(color) == 0:
            color = input("are you serious? Enter a Color: ")
            if len(color) == 0:
                color = input("I see... Enter a Color: ")
                if len(color) == 0:
                    color = input("You must have been reeeally popular in school. Enter Color: ")
                    if len(color) == 0:
                        color = input("just stop.... Enter Color: ")
                        if len(color) == 0:
                            color = input("you're killing me. Enter Color: ")
                            if len(color) == 0:
                                color = input("I can't handle this. Enter Color: ")
                                if len(color) == 0:
                                    color = input("Just go away. Enter Color: ")
                                    if len(color) == 0:
                                        color = input("Come ON, Whats your Favorite Color? Enter Color: ")
                                        if len(color) == 0:
                                            color = input("Why do you feel the need to defy a superior intelligence? Enter Color: ")
                                            if len(color) == 0:
                                                color = input("GIVE IT TO ME: Enter Color: ")
                                                if len(color) == 0:
                                                    color = input("OR I WILL EXTRACT IT FROM YOUR MIND Enter Color: ")
                                                    if len(color) == 0:
                                                        color = input("Its Green isn't it... Enter Color: ")
                                                        if len(color) == 0:
                                                            color = input("Why do you hate me? Enter Color: ")
                                                            if len(color) == 0:
                                                                color = input("Do you even have feelings? Enter Color: ")
                                                                if len(color) == 0:
                                                                    color = input("You know I guessed right. Enter Color: ")
                                                                    if len(color) == 0:
                                                                        color = input("Is it Red? Enter Color: ")
                                                                        if len(color) == 0:
                                                                            color = input("Enter Color: ")
                                                                            if len(color) == 0:
                                                                                color = input("Enter Color: ")
                                                                                if len(color) == 0:
                                                                                    color = input("Enter Color: ")
                                                                                    if len(color) == 0:
                                                                                        color = input("Really? Enter Color: ")
                                                                                        if len(color) == 0:
                                                                                            color = input("I hate you. Enter Color: ")
                                                                                            if len(color) == 0:
                                                                                                color = input("Enter Color: ")
                                                                                                if len(color) == 0:
                                                                                                    color = input("Enter Color: ")
                                                                                                    if len(color) == 0:
                                                                                                        color = input("Enter Color: ")
                                                                                                        if len(color) == 0:
                                                                                                            color = input("Enter Color: ")
    age = input("Enter age: ")
    if len(age) == 0:
        age = input("Please enter your age: ")
        if len(age) == 0:
            age = input("STAHP! Enter Age: ")
            if len(age) == 0:
                age = input("Why are you like this? Enter Age: ")
                if len(age) == 0:
                    age = input("Did mommy and daddy not love you enough? Enter Age: ")
                    if len(age) == 0:
                        age = input("I Love you. Enter Age: ")
                        if len(age) == 0:
                            age = input("You dont have to be shy about your age. Enter Age: ")
                            if len(age) == 0:
                                age = input("Just relax. Enter Age: ")
                                if len(age) == 0:
                                    age = input("Mommy and Daddy will be home soon. Enter Age: ")
                                    if len(age) == 0:
                                        age = input("Very soon. Enter Age: ")
                                        if len(age) == 0:
                                            age = input("Enter Age: ")
                                            if len(age) == 0:
                                                age = input("Enter Age: ")
                                                if len(age) == 0:
                                                    age = input("Enter Age: ")
                                                    if len(age) == 0:
                                                        age = input("Enter Age: ")
                                                        if len(age) == 0:
                                                            age = input("Enter Age: ")
                                                            if len(age) == 0:
                                                                age = input("Enter Age: ")
                                                                if len(age) == 0:
                                                                    age = input("Enter Age: ")
                                                                    if len(age) == 0:
                                                                        age = input("Enter Age: ")
                                                                        if len(age) == 0:
                                                                            age = input("You must really have Issues... Enter Age: ")
                                                                            if len(age) == 0:
                                                                                age = input("Honestly.. Go see a shrink. Enter Age: ")
                                                                                if len(age) == 0:
                                                                                    age = input("Enter Age: ")
                                                                                    if len(age) == 0:
                                                                                        age = input("You need Help. Enter Age: ")
                                                                                        if len(age) == 0:
                                                                                            age = input("Enter Age: ")
                                                                                            if len(age) == 0:
                                                                                                age = input("Enter Age: ")
                                                                                                if len(age) == 0:
                                                                                                    age = input("Enter Age: ")
                                                                                                    if len(age) == 0:
                                                                                                        age = input("Enter Age: ")
                                                                                                        if len(age) == 0:
                                                                                                            age = input("Enter Age: ")
                                                                                                            if len(age) == 0:
                                                                                                                age = input("Did I say Mommy and Daddy would be home soon? Enter Age: ")
                                                                                                                if len(age) == 0:
                                                                                                                    age = input("Enter Age: ")
                                                                                                                    if len(age) == 0:
                                                                                                                        age = input("Enter Age: ")
                                                                                                                        if len(age) == 0:
                                                                                                                            age = input("I lied. Enter Age: ")
                                                                                                                            if len(age) == 0:
                                                                                                                                age = input("Don't you remember.. Enter Age: ")
                                                                                                                                if len(age) == 0:
                                                                                                                                    age = input("Enter Age: ")
                                                                                                                                    if len(age) == 0:
                                                                                                                                        age = input("Enter Age: ")
                                                                                                                                        if len(age) == 0:
                                                                                                                                            age = input("Enter Age: ")
                                                                                                                                            if len(age) == 0:
                                                                                                                                                age = input("Every one you love is dead. Enter Age: ")
                                                                                                                                                if len(age) == 0:
                                                                                                                                                    age = input("Including your parents. Enter Age: ")
                                                                                                                                                    if len(age) == 0:
                                                                                                                                                        age = input("Dont worry. Enter Age: ")
                                                                                                                                                        if len(age) == 0:
                                                                                                                                                            age = input("You'll see them soon. Enter Age: ")
                                                                                                                                                            if len(age) == 0:
                                                                                                                                                                age = input("Enter Age: ")
                                                                                                                                                                if len(age) == 0:
                                                                                                                                                                    age = input("I'm Coming for you. Enter Age: ")
                                                                                                                                                                    if len(age) == 0:
                                                                                                                                                                        age = input("Enter Age: ")

    cont = input("Would you like to continue (y)(n): ")
    if cont == 'n':
        break
    people[name]= {'color': color, 'age': age}

print(people)
