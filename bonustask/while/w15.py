a= int(input())
ar= [0,1]
ind=0
k=0
while k<=a:
    k=ar[ind]+ar[ind+1]
    ar.append(k)
    ind+=1
for i in range(len(ar)):
    if ar[i]==a:
        print(i)
        break
    if i==len(ar)-1 and ar[i]!=a:
        print(-1)