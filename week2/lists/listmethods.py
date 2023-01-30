pf = ["Pink Floyd", "Metallica", "RHCP"]
new= [1,2,3]
pf.append(new)
print(pf)
new.clear()
print(new)

newl = pf.copy()
print(newl)

print(pf.count("RHCP"))

list1 = [True,False,True]
pf.extend(list1)
print(pf)

print(pf.index("RHCP"))

pf.pop(3)
pf.insert(3, "Oasis")
print(pf)

pf.remove("Metallica")
print(pf)

del pf[3:]

pf.sort()
print(pf)

pf.reverse()
print(pf)

