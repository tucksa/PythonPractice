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