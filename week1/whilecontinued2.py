# Populate the "prisoners" Dictionary with data from user input.
# prisoners = {<id>: { name: <name>, cell: <cell>},....}
# 1) create the Dictionary

prisoners = {}

while True:
    ID = input('Enter ID: ')
    if ID == "":
        break
    name= input('Enter Name: ')
    cell= input("cell: ")

    prisoners[ID] = {'name': name, "cell": cell}

print(prisoners)
