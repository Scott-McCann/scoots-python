nameList = []
name = "none"

while name:
    name = input("Enter your name: ")
    if name:
        nameList.append(name)

while nameList:
    print("Hello, " + nameList.pop() + "!")

print("All done")



iters = 10
while iters:
    print("iter number: " + str(iters))
    iters = iters - 1   
