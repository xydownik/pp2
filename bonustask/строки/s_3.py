s = input()
a = len(s)
if a%2!=0:
    x = a//2 +1
else:
    x = a//2
s1 = ""
s2 =""
for i in range(0,x):
    s1+= s[i]
for i in range(x,a):
    s2 += s[i]
print(s2+s1)