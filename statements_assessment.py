#1- print out only the words that start with 's' in the sentece
sentence = 'Print out only the words that start wit s in the sentence'
statement = sentence.split(' ')
for words in statement:
    if words[0].lower() == 's':
        print(words)

#2- use range to print out the numbers from 0-10
my_list = [num for num in range(0,11)]
print(my_list)

#3- use list comprehension to make a list of number from 1-50 that is divisible my 3
comp_list = [num for num in range(1,51) if num%3 == 0]
print(comp_list)

#4- go through the list and if the length of the word is even then print "even!"
st = 'Print every word in this sentence that has an even number of letters'
words4 = st.split(' ')
for i in words4:
    if len(i)%2 == 0:
       print('even!')

#5- print out numbers from 1-100 but for multiples of 3 print out Fizz, for multiples of 5 print out Buzz and for multiples of 3 and 5 print out FizzBuzz
FizzBuzz = [num for num in range(1,101)]
for i in FizzBuzz:
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)

#6- use list comprehension to create a list of the first letters from each word below
st = 'Create a list of the first letters of every word in this string'
word6 = st.split(' ')
first_letters = [letter[0] for letter in word6]
print(first_letters)