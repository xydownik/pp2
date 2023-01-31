# how many repeated numbers
a= int(input())
b = int(input())
c= int(input())
if (a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b):
    print(2)
elif a==b==c:
    print(3)
else:
    print(0)