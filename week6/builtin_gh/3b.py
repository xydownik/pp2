s = input()
a =[]
for i in s:
    a.append(i)
a  = reversed(a)
s2=""
for i in a:
    s2+=str(i)
if s==s2:
    print("palindrome")
else:
    print("not palindrome")
    
    
