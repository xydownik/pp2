j=1
mx=0
a=[]
while j!=0:
    x=int(input())
    j=x
    mx = max(j,mx)
    a.append(x)
i=0
cnt=0
while i<len(a):
    if a[i]==mx:
        cnt+=1
    i+=1
print(cnt)