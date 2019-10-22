#make a function that takes a string as a parameter and turns it to pig latin=> if the word starts with a vowel then add 'ay' to the end. if it does not then take the first letter, move to the end and add 'ay'

def pig_latin(st = 'Pig Latin'):
    sentence = st.split(' ')
    pig_sentence = ''
    for i in sentence:
        if i[0] in ['a','e','i','o','u']:
           pig_sentence += i + 'ay ' 
        else:
           pig_sentence += i[1:] + i[0] + 'ay '
    return pig_sentence


result = pig_latin('Hello my name is')
print(result)

#use *args to take in an arbitrary amount of arguments and will return tuples
def myfunc(*args):
    print(sum(args))

myfunc(3,6,22,10)

#similarly, use **kwargs to get arbitraty amount of key/value arguments returned as a dictionary
def secondfunc(**kwargs):
    print(kwargs)

secondfunc(fruit = 'bananas', veggie = 'brocoli')

def myformat(word):
    i = 0
    newWord = ''
    for letter in word:
        if i%2 == 0:
            newWord += letter.upper()
            i += 1
        else:
            newWord += letter.lower()
            i += 1
    print(newWord)

myformat('note')

#Lesser of Two Evens => return the lesser of two given even numbers if both are even, but return the greater if one or both are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        print('they are even! So here is the lesser:')
        if a > b:
            print(b)
        else:
            print(a)
    else:
        print('one of them is not even... so here is the greater:')
        if a > b:
            print(a)
        else:
            print(b)

lesser_of_two_evens(2,3)

#Animal Crackers => write a function that takes a two word string and returns True if both words begin with the same letter

def animal_crackers(st):
    word1 = st.split(' ')[0]
    word2 = st.split(' ')[1]
    print(word1[0].lower() == word2[0].lower())

animal_crackers('Laughing llama')

#The Other Side of Seven => given a value, return a value that is twice as far away on the other side of 7
def other_side_of_seven(x):
    difference = 7-x
    if difference >= 0:        
        print( 7 + (difference*2))
    else:
        print(7- (abs(difference)*2))

other_side_of_seven(12)

#Old Macdonald => write a function that capitolizes the first and fourth letters of a name
def old_macdonald(name):
    i= 0
    cap_name = ''
    for letter in name:
        if i == 0 or i == 3:
            cap_name += letter.upper()
            i += 1
        else:
            cap_name += letter
            i += 1
    print(cap_name)

old_macdonald('macdonald')