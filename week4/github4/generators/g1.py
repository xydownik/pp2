
n = int(input())
def square(n):
    a=0
    while a**2<=n:
       yield a**2
       a = a+1
for i in square(n):
    print(i)