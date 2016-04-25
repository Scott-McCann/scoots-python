# comprehensions and generators

sentence = "List Comprehensions are the Greatest!"
vowels = ('a','e','i','o','u')


new_sentence = ''.join([letter for letter in sentence if letter not in vowels])

print(new_sentence)

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
