#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)
x = people.index(str(input("Choose a person from the list to replace: ")))
people.pop(x)
y = str(input("Enter the replacement: "))
people.insert(x, y)
print(people)