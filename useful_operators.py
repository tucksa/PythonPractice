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