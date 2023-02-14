#2
class Shape(object):
    def area(self,a,b):
        if a =='' and b=='':
            print(0)
        else:
            self.s = int(a)*int(b)
            print(self.s)
class Square(Shape):
    def __init__(self,length):
        self.length = length
        Shape.area(self,self.length,self.length)  
ex1 = Square(4)
#3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        Shape.area(self, self.length,self.width)
ex2 = Rectangle(4,5)