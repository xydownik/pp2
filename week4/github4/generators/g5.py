n = int(input())
def down(n):
    a = n
    while a!=-1:
        yield a
        a-=1
for i in down(n):
    print(i)