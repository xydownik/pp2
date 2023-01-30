tuple1 = ("Pink Floyd", "Metallica", "RHCP","Led Zeppelin","Fleetwood Mac", "Placebo")
l = list(tuple1)
l[-3] = "Prog Rock"
tuple1 = tuple(l)
print(tuple1)

l.append("Oasis")
tuple1 = tuple(l)
print(tuple1)

l = ("Heavy Rock",)
tuple1 += l
print(tuple1)

l = list(tuple1)
l.remove("Metallica")
tuple1 = tuple(l)
print(tuple1)

del tuple1
print(tuple1) #Error: not found
