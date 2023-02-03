a =int(input())
b = int(input())
s =""
if(a%2==0):
    for i in range(a-1,b-1,-2):
        s+=str(i) + " "
else:
    for i in range(a,b-1,-2):
        s+=str(i) + " "
print(s)