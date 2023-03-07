import re
file = open("C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week5/text.txt", "r") 
# 1) Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s  
# result = re.findall(".*a.*b*", file.read())
# print(result)

# 2)Write a Python program that matches a string that has an 'a' followed by two to three 'b'
# result = re.findall(".*a.*b.*b.*b?.*", file.read())
# print(result)

# 3)Write a Python program to find sequences of lowercase letters joined with a underscore.
# result = re.findall("(([a-z]+_)(_?[a-z]+)+)+", file.read())
# print(result)

# 4)Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# result = re.findall("[A-Z][a-z]+", file.read())
# print(result)

# 5)Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# result =re.findall(".*a.*b$", file.read())
# print(result)

# 6)Write a Python program to replace all occurrences of space, comma, or dot with a colon.
# result = re.sub("[ ,.]", ":", file.read())
# print(result)

# 7)Write a python program to convert snake case string to camel case string
# s = "wdefsf_aefsgdfba_acdsv_cds_DSVF_w"
# l = re.split(r"_", s)
# res = ''
# for i in l:
#     res += (i[0].upper() + i[1:])
# print(res)

# 8)Write a Python program to split a string at uppercase letters.
# result=re.split("[A-Z]",file.read())
# print(result)

# 9)Write a Python program to insert spaces between words starting with capital letters.
# result=re.findall("[A-Z]{1}[a-z]\w*",file.read())
# print(result)

# 10)Write a Python program to convert a given camel case string to snake case.
# s= "WdefsfAefsgdfbaAcdsvCdsDSVFW"
# l = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
# res = re.sub("([a-z0-9])([A-Z])", r"\1_\2", l).lower()
# print(res)