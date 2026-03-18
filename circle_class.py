import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area (self):
        return math.pi*self.radius**2
    def circumference(self):
        return 2*math.pi*self.radius

my_circle=circle(int(input("Enter the radius of the circle: ")))
print("The area of the circle is:", my_circle.area())
print("The circumference of the circle is", my_circle.circumference())
