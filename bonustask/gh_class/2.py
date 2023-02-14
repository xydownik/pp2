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
