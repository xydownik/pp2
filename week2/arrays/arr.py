l1 = ["Pink Floyd", "Metallica","RHCP"]
l2 = ["Placebo", "Grateful dead"]

print(l1[0])
l1[0] = "PF"
print(l1[0])

x= len(l1)
print(x)

for x in l1:
    print(x)
    
    
#array methods
l1.append("Tame Impala")
print(l1)

l1.pop(2)   
print(l1) 

l1.remove("PF")
print(l1)

l1.append("Led Zeppelin")
print(l1)

l2.clear()
print(l2)

l2 = l1.copy()
print(l2)

x =l2.count("Led Zeppelin")
print(x)

l1.extend(l2)
print(l1)

x = l1.index("Tame Impala")
print(x)

l1.insert(1,"PF")
print(l1)

l1.pop(6)
print(l1)

l1.remove("Tame Impala")
print(l1)

l1.reverse()
print(l1)

l1.sort()
print(l1)