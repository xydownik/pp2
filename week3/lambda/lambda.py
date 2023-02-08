x = lambda a : a**3
print(x(10))

x = lambda a,b : a*b
print(x(2,3))

x = lambda a, b, c : a+b+c
print(x(1,2,3))

def func(n):
    return lambda a : a*n
num = func(2)
print(num(3))

def degree(n):
    return lambda a : a**n
square = degree(2)
thirddeg = degree(3)
print(square(10))
print(thirddeg(12))