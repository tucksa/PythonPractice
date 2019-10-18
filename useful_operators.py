#range(start,stop,step)

#create a list 1-25
example = []
for i in range(1,26):
    example.append(i)
print(example)

#or cast it to a list using list()
print(list(range(1,26,2)))

#Enumerate

#Here is the long hand way of doing it
index = 0
for letter in 'abcde':
    print(f'At index {index} the letter is {letter}')
    index += 1

#with enumerate 
word = 'abcde'
for item in enumerate(word):
    print(item)

#this returns a tuple so you can unpack it
for index,letter in enumerate(word):
    print(f'Index: {index}\nLetter: {letter}')

# the zip function will match together lists. note- it will go the length of the shortest list
list1 = [1,2,3,4,5,6]
list2 = ['a','b','c']
list3 = ['x', 'y', 'z']

for item in zip(list1, list2, list3):
    print(item)

#use in to get boolean check
print('a' in 'Sarah')

print(1 in list3)

car = {'make': 'Toyota', 'model': 'Prius', 'color': 'silver'}
print('model' in car)

#remember .values() if you want to check if it exists in the values
print('silver' in car.values())

#min and max 
my_list = [12,2,4,8,25,80,6,16]
print(min(my_list))
print(max(my_list))

#useful library - random
from random import shuffle
shuffle(my_list)
print(my_list)
#shuffle doesn't return anything, but instead works in place on the list

#use randint to return a random integer in (min, max) range
from random import randint
print(randint(1,100))

#input can be received from the user
result= input('What is your name? ')
print(result)

#note that this always returns a string.... so you may have to adjust

fav_num= int(input('What is your favorite number? '))
print(fav_num)