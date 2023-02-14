#4
def filter_prime(l1):
    l2=[]
    for i in l1:
        count=0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                count+=1
        if count==0:
            l2.append(i)
    print(l2)
n=list(map(int,input().split()))
filter_prime(n)