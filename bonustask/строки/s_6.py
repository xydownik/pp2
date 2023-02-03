s =input()
x = s.find("f")
b=-1
for i in range(x+1, len(s)):
    if s[i]=="f":
        b=i
        break
if s.find("f")==-1:
    print(-2)
else:
    print(b)        
        
