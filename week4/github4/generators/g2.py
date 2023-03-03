n = int(input())
def Even(n):
    a=0
    while a<=n:
        yield str(a)+', ' 
        a+=2
result =""
for i in Even(n):
    result+=i
result = result[:-2]
print(result)