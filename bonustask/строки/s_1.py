s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
s2 =""
i=0
while i<len(s):
    if i%2==0:
        s2+= s[i]
    i+=1
print(s2)
s2 =""
j=0
while j<len(s):
    if j%2==1:
        s2 += s[j]
    j+=1
print(s2)

s = s[::-1]
print(s)
i=0
s2=""
while i<len(s):
    if i%2==0:
        s2+=s[i]
    i+=1
print(s2)

print(len(s))