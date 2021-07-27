#To find the area of rectangle using classes
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
areaofrectangle = rectangle(l, b)
print("Area of rectangle:", areaofrectangle.area())