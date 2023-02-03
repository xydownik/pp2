n = int(input())
i = 0
x=1
while x<=n:
    i+=1
    x = 2**i
i-=1
x//=2   
print(i,x)