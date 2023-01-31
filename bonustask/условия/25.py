#min from 3 numbers
a = int(input())
b = int(input())
c= int(input())
a1 = []
a1.append(a)
a1.append(b)
a1.append(c)
min = 1e9
for x in a1:
    if x< min:
        min = x
print(min)