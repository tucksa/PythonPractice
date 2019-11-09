#Use error handling to allow your code to continue even after an error has occured
try_def = 'This is the block of code to be attempted (may lead to an error)'
except_def = 'Block of code will execute in case there is an error in the try block'
finally_def = 'A final block of code to be executed, regardless of an error.'

try:
    #want to attempt this code
    result = 10 + '10'
except: 
    #want if the attempted code fails
    print('Hey it looks like you are not adding correctly')
else: 
    #want if the code does run correctly
    print('Add went well')
    print(result)
finally:
    #want to run no matter what happens with the try
    print('I always run')

#in this case the try will fail b/c you cant add an int and a str so you will get "Hey it looks like you are not adding correctly" combined with the finally block as always

try:
    #want to attempt this code
    result = 10 + 10
except: 
    #want if the attempted code fails
    print('Hey it looks like you are not adding correctly')
else: 
    #want if the code does run correctly
    print('Add went well')
    print(result)
finally:
    #want to run no matter what happens with the try
    print('I always run')

#In this case python wont have any trouble with the try so you will output "Add went well" and the result combined with the finally block as always

#Homework:
# Handle the exception thrown by the code below by using try and except blocks.
#for i in ['a','b','c']:
    #print(i**2)

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('You got some kind of erro on the try code but we can keep going')
finally:
    print('see- not a problem')

# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
#x = 5
#y = 0
#z = x/y

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('You got a ZeroDivisionError... you can even specify what to run to which type of error. custom!')
except:
    print('this will go for any other kind of error from the try')
finally:
    print('All Done.')


# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            result = (int(input('Give me a number to square: ')))**2
        except:
            print('Thats not a number.... I will ask you again')
            continue 
        else:
            print(result)
            break

ask()