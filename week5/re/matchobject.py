import re
txt = "The rain in Spain"

# .span() returns a tuple containing the start-, and end positions of the match
x = re.search(r"\bS\w+", txt)
print(x.span())

# .string() returns the string passed into the function
x = re.search(r"\bS\w+", txt)
print(x.string)

# .group() returns the part of the string where there was a match
x = re.search(r"\bS\w+", txt)
print(x.group())