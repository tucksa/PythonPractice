#Object Oriented Programming (OOP) allows programmers to create their own objects tat have methods and attributes
# OOP creates code that is repeatable and organized 

# class NameOfClass():
#   def _init_(self, param1,param2):
#       self.param1 = param1
#       self.param2 = param2
#   def some_method(self):
#       print(self.param1)

#create attributes = characteristics of the object. functions inside this class = method
class Dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

#create an instance of this class:
my_dog = Dog('Labrador', 'Jessie', 5)
print(type(my_dog))
print(my_dog.breed)

#Class object attribute
class Dog2:
    species = 'mammal'
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

my_dog = Dog2('Labrador', 'black', 7)
your_dog = Dog2('Poodle', 'white', 2)
#print both instances and see that species is held 
print(my_dog.breed)
print(my_dog.species)
print(your_dog.breed)
print(your_dog.species)

#methods- a function ocurring inside a class
class Dog3:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    def bark(self):
        print(f'Woof! My name is {self.name}')

puppy = Dog3('Pit bull', 'Chunk')
puppy.bark()

#using inheritance to reuse defined class info
class Animal:
    def __init__(self):
        print('animal created')
    def eat(self):
        print('I am eating')
    def sleep(self):
        print("I am sleeping")

class Dog4(Animal):
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

#your instance of Dog4 can pull from Animal
my_dog = Dog4('Lab', 'Tucker')
my_dog.eat()
my_dog.sleep()

#Abstract methods
class Animal2:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog5(Animal2):
    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal2):
    def speak(self):
        return self.name + ' says meow!'

fido = Dog5('Fido')
felix = Cat('Felix')

print(fido.speak())
print(felix.speak())
