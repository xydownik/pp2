pf = ["Pink Floyd", "Metallica", "RHCP","Led Zeppelin","Fleetwood Mac", "Placebo"]
new = []
for x in pf:
    if "e" in x:
        new.append(x)
print(new)

newl = [x for x in pf if "d" in x]
print(newl)
newl = [x for x in pf if x != "RHCP"]
print(newl)
newl = [x for x in pf]
print(newl)
newl = [x for x in range(10)]
print(newl) 
newl = [x for x in  range(20) if x < 15]
print (newl)
newl = [x.upper() for x in pf]
print(newl)
newl = [ "great music" for x in pf]
print(newl)
newl = [x if x!= "Fleetwood Mac" else "Oasis" for x in pf]
print(newl)
