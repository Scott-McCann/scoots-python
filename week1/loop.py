# create a lists
# prompt the user to enter 10 name

nameList = []
name = "none"
iters = 10
while iters:
  name = input("enter name: ")
  nameList.append(name)
  iters = iters -1

while nameList:
  print("Hello, " +nameList.pop()+"1")

print("finshed")
