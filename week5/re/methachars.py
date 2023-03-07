import re
txt = "The rain in Spain"

# [] A set of characters
x = re.findall("[a-m]", txt)
print(x)
# . Any character
txt2 = "hello planet"
x = re.findall("he..o", txt2)
print(x)
# ^ Starts with
x = re.findall("^hello", txt2)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
# $ Ends with
x = re.findall("planet$", txt2)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# * zero or more occurences
x = re.findall("he.*o", txt2)
print(x)

# + one or more occurences
x = re.findall("he.+o", txt2)
print(x)

# ? zero or one occurence
x = re.findall("he.?o", txt2)
print(x)

#{} exactly the specified times of occurence
x = re.findall("he.{2}o", txt2)
print(x)

# | either or
txt3 = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt3)
print(x)

# capture and group
