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
