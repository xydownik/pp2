s = input()
a = s.find("h")
b = s.rfind("h")
s1 = ""
s2=""
s3=""
for i in range(len(s)):
    if i<=a:
        s1+=s[i]
    elif i>=b:
        s3+=s[i]
    else:
        s2+=s[i]
s2 = s2.replace("h","H")
print(s1+s2+s3)