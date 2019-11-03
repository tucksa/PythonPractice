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

