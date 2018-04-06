# area of rectangle using class
class Rect:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        
        return self.length*self.breadth
    
a = int(input("enter the length"))
b = int(input("enter the breadth"))
obj = Rect(a,b)
print("Area:",obj.area())
