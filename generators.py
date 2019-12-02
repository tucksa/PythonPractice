#Generator functions will automatically suspend and resume their execution and state around the last point of value generation
#An example of this would be range(1,10)- this does not store all the values but instead it only remembers the last value 

#here is an example of when you might want to save memory and use a generator
def cubed(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result
for x in cubed(10):
    print(x)

#here is this same result written as a generator so you do not need to store the result as an array and waste memory
def cubed_gen(n):
    for i in range(n):
        yield i**3

for num in cubed_gen(10):
    print(num)

#you can use next() to step through the values 
def gen_fibon(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a,b = b,a+b

num = gen_fibon(10)

print(next(num))
#output = 1
print(next(num))
#output = 1
print(next(num))
#output = 2
print(next(num))
#output = 3
print(next(num))
#output = 5

#note it will not allow you to execute next() on a string, but you can force the string into a iterable by using iter()
st = 'hello'
#if you tried next(st) it would output a type error
st_iter = iter(st)
print(next(st_iter))
#output = h
print(next(st_iter))
#output = e

#Generator HW:

#1- Create a generator that generates the square of numbers up to some number 'n'
def gensquares(n):
    for i in range(n):
        yield i**2
for num in gensquares(10):
    print(num)

#2- Create a generator that yields 'n' random numbers between a low and high range (arguments recieved from user)
def rand_num(low,high,n):
    import random 
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

#3- Use iter() function to convert the string below into an interator:
s = 'hello'
s_iter = iter(s)
print(next(s_iter))