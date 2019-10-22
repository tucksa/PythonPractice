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