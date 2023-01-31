l1 = ["Pink Floyd", "Metallica","RHCP"]
l2 = ["Placebo", "Grateful dead"]
for  i in l1:
    print(i)

for x in l1:
    print(x)
    if x=="Metallica":
        break

for x in l1:
    if x == "Metallica":
        break
    print(x)
    
for x in l1:
    if x == "Metallica":
        continue
    print(x)
print("\n")

for x in range(11):
    print(x)
print("\n")

for x in range(5,11):
    print(x)
print("\n")
    
for x in range(5,12,2):
    print(x)
print("\n")    

for x in range(11):
    print(x)
else:
    print("Ended")
print("\n")

for x in range(11):
    if x == 5:
        break
else:
    print("Ended")
print("\n")

for i in l1:
    for j in l2:
        print(i,j)
print("\n")

for i in [0,1,2]:  # having an empty for loop like this, would raise an error without the pass statement
    pass
    
    
