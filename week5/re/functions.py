import re
#findall()
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#search()
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

#split()
x = re.split("\s", txt)
print(x)

    #Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#string
x = re.search(r"\bS\w+", txt)
print(x.string)

#sub()
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)