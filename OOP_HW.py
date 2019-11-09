#create a class for a line that includes methods to find the distance and slope of the line
class Line:
   
    def __init__(self, coor1,coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        import math
        return math.sqrt((self.x2-self.x1)**2 + (self.y2- self.y1)**2)

    def slope(self):
        return (self.y2-self.y1) / (self.x2-self.x1)

li = Line((3,2), (8,10))
print(li.distance())
print(li.slope())

# make a class that defines a cylinder and has methods to calculate volume and surface area

class Cylinder:
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius 
        self.pi = 3.14
    
    def volume(self):
        return (self.pi * self.height * (self.radius**2))

    def surface_area(self):
        return ((2 * self.pi * self.radius * self.height) + (2 * self.pi * (self.radius**2)))

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())

#OOP Challenge: create an object representing a bank account with two attributes(owner and balance) and two methods (deposit and withdraw). 
#withdrawals cannot exceed the balance

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of {amount} successful. Your new total is {self.balance}')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal of {amount} successful. Your new total is {self.balance}')
        else:
            return f'You have exceeded your total balance of {self.balance}'
    def __str__(self):
        return f'Owner: {self.owner}\nBalance: {self.balance}'
bank1 = Account('Sarah', 500)

print(bank1)

bank1.deposit(50)
bank1.withdraw(100)
