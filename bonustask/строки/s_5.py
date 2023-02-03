s =input()
x= s.count("f")
if x==1:
    print(s.find("f"))
elif x>1:
    print(s.find("f"),s.rfind("f"))