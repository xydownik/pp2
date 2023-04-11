n = int(input())
a = []
b=[" "]
s= ""
s1 ="*"
j=n-1
for i in range(1,n+1): 
        s2 = " "*j 
        s = s2 +s1*i 
        a.append(s) 
        j-=1
s3= ""
for i in range(0,n-1):
    s3 += s1 
    b.append(s3)
for i in range(len(a)):
    print(a[i],b[i],sep ="")
