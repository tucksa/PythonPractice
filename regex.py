# Regular Expressions
#   text-matching patterns described with a formal syntax. 

#Searching for pattersn in text- use the re module
import re 
#list of patterns to search for
patterns = ['hi', 'hello', 'hey']
#text to search through
text = 'Hello and hey there. I hope you are having an excellent day!'
#loop through patterns to search
for pattern in patterns:
    print(f'Searching for {pattern} in:\n"{text}"\n')
    #check for a match
    if re.search(pattern,text):
        print('Match found!')
    else:
        print('No match found ...')
#note that the search is case sensetive so you would have to use text.lower() to catch Hello as a match to hello

#re.search(pattern,text) returns an object not just a boolean
pattern2 = 'Hello'
text2 = 'Hello World!'
match = re.search(pattern2,text2)
print(type(match))
#you can see at what index the match starts and ends for example
print(match.start())
print(match.end())

#Split with regular expression
split_term = '@'
email = 'tuckerjsarah@gmail.com'
split = re.split(split_term, email)
print(split)

#Find all instances of a pattern
count = re.findall('the', 'the fox jumped over the fence and almost made it to the moon')
print(len(count))

#re Pattern syntax: you can use metacharacters with re to find patterns
def multi_re_find(patterns, phrase):
    '''
    Takes in a list of regex patterns
    prints a list of the matches
    '''
    for pattern in patterns:
        print(f'Searching the phrase using the re check: {pattern}')
        print(re.findall(pattern, phrase))
        print('\n')

#Ways to express repetition in a pattern:
'''
    - * is repeated zero or more times
    - + is repeated one or more times
    - ? is repeated zero or one time
    - {n} is repeated n number of times
    - {n,m} is repeated a minimum of n times and a maximum of m times
'''
test_phrase = 'abab...aaabbb...abbbabbb...baba...baaaa...abbbb'
test_patterns = ['ab*', #a followed by zero or more bs
                 'ab+', #a followed by one or more bs
                 'ab?', #a followed by zero or one b
                 'ab{3}', #a followed by 3 bs
                 'ab{2,3}' #a followed by at least 2 bs and at most 3 bs
                ]
multi_re_find(test_patterns, test_phrase)

#use brackets to search for character sets
test_patterns2 = ['[ab]', #either a or b
                  'a[ab]+' #a followed by one or more a or b                
                ]
multi_re_find(test_patterns2, test_phrase)

#Exclusion using ^ in brackets
sentence = 'This is a string! But it has punctuation. How can we remove it?'
#use the + to check that the match appears at least once
print(re.findall('[^!.,? ]+', sentence))

#Character ranges- you can use [start-end] to look for characters in a range
string = 'This is an example sentence. Lets see if we can find some letters'
search_patters = ['[a-z]+', #sequences of lower case letters
                  '[A-Z]+', #sequences of upper case letters
                  '[a-zA-Z]+', #sequences of lower or upper case letters
                  '[A-Z][a-z]+' #sequences of one upper case followed by lower case letters
                ]
multi_re_find(search_patters, string)

#Escape codes- you can use special escape codes to find specific types of patterns
'''
    - \d for a digit
    - \D for a non-digit
    - \s for whitespace
    - \S for non-whitespace
    - \w for alphanumeric
    - \W for non-alphanumeric
'''
test_phrase2 = 'This is a string with some numbers 1233 and a symbol #hashtag'
# python arleady uses \ as an escape but we can get around that by putting an r in front
test_patterns3 = [r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']
multi_re_find(test_patterns3, test_phrase2)