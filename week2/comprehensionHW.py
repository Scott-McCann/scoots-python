# remove the vowels from the sentence
sentence = "List Comprehensions are the Greatest!"
vowels = ('a','e','i','o','u')


new_sentence = ''.join([letter for letter in sentence if letter not in vowels])

print(new_sentence)



#get an average for each studen
grades = {'Inara': {'Homework 1': 90, 'Homework 2': 94, 'Homework 3': 90},
          'Mal': {'Homework 1': 50, 'Homework 2': 100, 'Homework 3': 60},
          'Simon': {'Homework 1': 98, 'Homework 2': 96, 'Homework 3': 96},
           'River': {'Homework 1': 100, 'Homework 2': 100, 'Homework 3': 0}}

def average(names):
    total=0
    for homework in grades[names]:
        total += grades[names][homework]
    return int(total) / len(grades[names])

meanGrades = {name: average(name) for name in grades}


print(meanGrades)




#find all words that end with 'ace' print with statement.
wordlist = []
with open('/usr/share/dict/words', 'r') as dictionary:
    # for line in dictionary:
    #     word = line.strip()
    #     if word.endswith("ace"):
    #         wordlist.append(word)

    wordlist = [line.strip() for line in dictionary if line.endswith('ace\n')]

print(wordlist)

for word in wordlist:
    print(word + " Ventura, pet detective!")




#use nested dictionary Comprehensions to get the average of homework 3
homework3 = sum([grades[name]['Homework 3'] for name in grades]) / len(grades)

print(homework3)
