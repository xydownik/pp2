import re
txt = "The rain in Spain"
# \A char is at the beginning 
x = re.findall("\AThe", txt)
print(x)

#\b at the beginning or end. (the "r" in the beginning is making sure that the string is being treated as a "raw string")
x = re.findall(r"\bain", txt)
print(x)
x = re.findall(r"ain\b", txt)
print(x)

# \B present but NOT at the beginning
x = re.findall(r"\Bain", txt)
print(x)
x = re.findall(r"ain\B", txt)
print(x)

# \dreturnes strings containing digits [0-9]
x = re.findall("\d", txt)
print(x) 

# \D doesn't contain digits
x = re.findall("\D", txt)
print(x)

#\s contains a white space
x = re.findall("\s", txt)
print(x)

#\S non-white-space  chars
x = re.findall("\S", txt)
print(x)

#\w  contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character
x = re.findall("\w", txt)
print(x)

# \W DOES NOT contain any word characters (characters NOT between a and Z. Like "!", "?" white-space etc.)
x = re.findall("\W", txt)
print(x)

# \Z specified characters are at the end of the string
x = re.findall("Spain\Z", txt)
print(x)