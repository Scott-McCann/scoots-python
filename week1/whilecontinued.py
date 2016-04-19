nameList = []
name = 'default'

while name:
  name = input("Enter name: ")
  if len(name) < 2:
      nameList.append(name)

print(nameList)

while nameList:
    name = nameList.pop()
    if not name:
        continue

    print("Hello, " + name)
