# chess desk
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
a = a1+a2
b = b1+b2
if a%2==0 and b%2==0:
    print("YES")
elif a%2==1 and b%2==1:
    print("YES")
else:
    print("NO")