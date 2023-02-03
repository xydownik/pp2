n=int(input())
a=[0,1]
ind=0
j=2
while j<=n:
    k=a[ind]+a[ind+1]
    a.append(k)
    j+=1
    ind+=1
    
print(a[n])