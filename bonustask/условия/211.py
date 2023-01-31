#конь
a1= int(input())
a2=int(input())
b1=int(input())
b2=int(input())
if (abs(a1-b1)==1 and abs(a2-b2)==2) or (abs(a1-b1)==2 and abs(a2-b2)==1):
    print("YES")
else:
    print("NO")