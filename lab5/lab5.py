"""
Claudio Lopez
lab 5: review of class. objects. methods, and attributes
Sep 16, 2026
"""
print("\n Example 1: ")
class Circle():
    def __init__(self,  radius, color):
        self.r = radius
        self.c = color

    pi = 3.14157
    def circumfrence(self):
        return 2*self.pi*self.r


c1 = Circle(2, "Red")
print(c1.c)
print(c1.circumfrence())

print("\n Example 2: ")
class Rectangle():
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2*self.w + 2*self.h

"""    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.w, self.h, fr=self.c))
        plt.axis('scaled')
        plt.show"""

r1 = Rectangle(2,3, "Pink")
print(r1.perimeter())

class Car():
    def __init__(self, Car1, Car2):
        self.c1 = Car1
        self.c2 = Car2
    maxspeed = 0
    mileage = 0
    defaultcolor = ""
    def firstcar(self):
        self.f = int(input("How many seats in this car: "))
        return self.f
    def secondcar(self):
        self.s = int(input("How many seats in this car: "))
        return self.s
    def maxmile1(self, max, mile):
        self.m = max
        self.mi = mile
    def maxmile2(self, max, mile):
        self.m2 = max
        self.mi2 = mile
    def display(self):
        print("Car 1:", self.c1, "has", self.firstcar(), "seats", "with a max mps of", self.m, "and mileage of",self.mi, "\n", "Car 2:", self.c2, "has", self.secondcar(), "seats", "with a max mps of", self.m2, "and mileage of", self.mi2)
w = Car("Rent", "Let")
Car.defaultcolor = "white"
w.maxmile1(200, 50000)
w.maxmile2(180, 75000)
w.display()