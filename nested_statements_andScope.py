x = 25

def printer():
    x = 50
    return x

print(x)
#this will return 25

print(printer())
#this will return 50

# SCOPE!!! LEGB rules in Python (the order python will check for variables)
# L: Local first (within a function)
# E: enclosing function locals
# G: Global
# B: Built-in Python

# Local example => lambda num: num**2. num is a local variable here

#Global
name = 'THIS IS A GLOBAL STRING'
def greet():
    #Enclosing
    name = 'Sammy'
    def hello():
        #Local
        name = 'IM A LOCAL'
        print('Hello '+ name)
    hello()
greet()

# Enclosing local is defining name as Sammy whereas global is the 'THIS IS A GLOBAL STRING' assignment

#Variables assigned inside a function are restricted by scope of that funciton
x = 50

def func(x):
    print(f'X is {x}')
    #local reassignment
    x = 200
    print(f'I just locally changed x to {x}')

func(x)
print(x)
#func(x) returns the two string literals with x as 50 then 200 respectively. print(x) returns x as 50 because its called in the global scope so it pulls the global assignment