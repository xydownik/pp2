i=0
j=1
k=1e9
while j!=0:
    x=int(input())
    j=x
    if j>k:
        i+=1
    k=j
print(i)