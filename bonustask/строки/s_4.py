s =input()
a= []
s1 = ""
s2= ""
for i in s:
    if i==" ":
        a.append(s1)
        s1 =""
        continue
    s1+=i
a.append(s1)
a.reverse()
for i in a:
    s2+=i + " "
print(s2)