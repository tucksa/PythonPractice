#decorators => allows you to tack on extra functionality to an already existing function

#example layout:

#    @some_decorator
#   def simple_func():
#       do suff
#       return something

#In python, you can return a function from a function and save it to a variable
def say_hello():
    print('you are running the hello func')
    def greet():
        print('It is nice to meet you!')
    return greet
#now you can save greet as a variable greetings and call it anywhere
greetings = say_hello()
greetings()
#this returns the 'it is nice to meet you' phrase from running the greet function within say_hello

#you can also pass a funtion into another function as an argument
def hello_world():
    print('Hello World!')

def other(some_func):
    print('Here is the work of my other function')
    print(some_func())

other(hello_world)
#this prints out the initial print statement in other func and the print statement in the argument func 'hello_world'

#Using this we can create a decorator
def new_decorator(original_func):
    #think of this as wrapping your original code in other coder
    def wrap_func():
        print('Some extra code before the original function')
        original_func()
        print('Some extra code after the original function')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

#instead of all that though you can just use the @
@new_decorator
def func_needs_decorator():
    print('I want to be decorated')
func_needs_decorator()
#this returns the same thing as decorated_func()
#it allows you to easily turn off or on these added decorations
