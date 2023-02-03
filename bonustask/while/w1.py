n = int(input())
j=1
i=1
s= ""
while i<=n:
    s+=str(i) +" "
    j+=1
    i = j**2
print(s)