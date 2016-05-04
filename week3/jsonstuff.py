import requests
import json

def unicron(aList):
    NewList = []
    for item in aList:
        if item not in NewList:
            NewList.append(item)

    return NewList

    
root = "http://jsonplaceholder.typicode.com"


#Unique User IDs
postrequest = requests.get(root + "/posts")
PostData = postrequest.json()
print(postrequest)
userid = []



for item in PostData:
    userid.append(item['userId'])

print(userid)

uniqueid = unicron(userid)

print(uniqueid)
#
# print('''#########################################################################''')

#unique emails from post 12

commentrequest = requests.get(root + "/comments")
# print(commentrequest)
commentData = commentrequest.json()
emails = []
for item in commentData:
    if item['postId'] is 12:
        emails.append(item['email'])
print(emails)

#unique emails for posts 12-30
numlist = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
newEmails = []
for item in commentData:
    if item['postId'] in numlist:
        newEmails.append(item['email'])
uniqueNewEmails = unicron(newEmails)

print(newEmails)
