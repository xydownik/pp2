a=20
b=30
c=40

print("a<b") if a<b else print("a==b") if a==b else print("a>b") 


if b>a:
    if(b>c):
        print("b is gretaer than a and c")
    elif(b==c):
        print("b is greater than and equal to c")
    else:
        print("b is greater than a but smaller than c ")


if b>a or b>c:
    print("b is not the smallest element")
if c>a and c>b:
    print("c is the largest element")