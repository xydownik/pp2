j=1
a=[]
b=[]
ind=0
while j!=0:
    x=int(input())
    j=x
    if a==[]:
        a.append(j)
    elif a!=[]:
        if j == a[0]:
            a.append(j)
        else:
            b.append(len(a))
            a=[]
            a.append(j)
    ind+=1
print(max(b))
