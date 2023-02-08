class coord():
    x = 5
    y = 4
point = coord()
print(point.x, point.y)


class Person():
    def __init__(self, name,age):
        self.name  = name
        self.age = age
chel = Person("Ponimayu", 22)
print(chel.name, chel.age)

print(chel)

class person():
    def __init__(self, name,age):
        self.name  = name
        self.age = age
        
    def __str__(obj):
        return f"{obj.name}({obj.age})"
    
    def func(silly):
        print("Hello, my name is "+silly.name)
chel = person("Ponimayu", 22)
print(chel)
chel.func()

chel.age = 43
print(chel.age)

del chel.age
del chel

print(chel, chel.age) #error

class person:
    pass


