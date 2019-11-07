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