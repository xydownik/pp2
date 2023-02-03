s =input()
a = s.find("h")
b = s.rfind("h")
s1 = ""
for  i in range(len(s)):
    if i<a or i>b:
        s1+=s[i]
    else:
        continue
print(s1)