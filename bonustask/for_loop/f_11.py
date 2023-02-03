n = int(input())
sum1 = 0
for i in range(1,n):
    x = int(input())
    sum1+=x
sum2 = 0  
for i in range(1,n+1):
    sum2+=i
print(sum2-sum1)