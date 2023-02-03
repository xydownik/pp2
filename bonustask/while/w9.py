a=[]
j=1
mx=0
while j!=0:
    x=int(input())
    j=x
    mx = max(j,mx)
    a.append(x)

for i in range(len(a)):
    if a[i]==mx:
        print(i)
        break
