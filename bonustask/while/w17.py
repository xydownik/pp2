j=1
sum=0
cnt=0
a=[]
while j!=0:
    x =int(input())
    j=x
    if j!=0:
        sum+=j
        cnt+=1
        a.append(j)
s = sum/cnt
i=0
sum2=0
while i <len(a):
    sum2+=((a[i]-s)**2)
    i+=1
res = (sum2/(cnt-1))**(1/2)
print(res)