import re
txt = "The rain in Spain"

# contains any of the specified chars [xyz]:
x = re.findall("[arn]", txt)
print(x)

#a match for any lower case character, alphabetically between a and n
x = re.findall("[a-n]", txt)
print(x)

#a match for any character EXCEPT a, r, and n
x = re.findall("[^arn]", txt)
print(x)

#a match where any of the specified digits (0, 1, 2, or 3) are present
txt2 = "8 times before 11:45 AM"
x = re.findall("[0123]", txt2)
print(x)

#a match for any digit between 0 and 9
x = re.findall("[0-9]", txt2)
print(x)

#a match for any two-digit numbers from 00 and 59
x = re.findall("[0-5][0-9]", txt2)
print(x)

# a match for any character alphabetically between a and z, lower case OR upper case
x = re.findall("[a-zA-Z]", txt)
print(x)

#In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
x = re.findall("[+]", txt2)
print(x)