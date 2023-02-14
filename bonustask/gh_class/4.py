#4
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x};{self.y})")
    def move(self, x1,y1):
        self.x = x1
        self.y = y1
    def dist(self,x2,y2):
        return ((abs(self.x - x2)**2) +abs(self.y - y2)**2)**(1/2)  #diagonal of a rectangle made by two points
        

ex3 = Point(4,5)
ex3.show()
ex3.move(7,5)
ex3.show()
print(ex3.dist(3,3))