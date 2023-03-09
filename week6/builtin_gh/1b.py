list1 = [1,2,3]
i=1
it = iter(list1)
res= list1[0]
while i<=len(list1):
    res*=next(it)
    i+=1
print(res)

#P.S. I used these kind of complicated ways to use built-in functions. Otherwise I'd solve them in an easier way