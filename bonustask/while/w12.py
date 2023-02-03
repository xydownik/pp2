a=[]
j=1
mx=0
while j!=0:
    x=int(input())
    j=x
    mx = max(j,mx)
    a.append(j)
premax =0
i=0
while i<len(a):
    if a[i]!=mx:
        premax = max(a[i],premax)
    i+=1
print(premax)