dict1 = {
    "Album" : "The dark side of the moon",
    "Group" : "Pink Floyd",
    "Genre" : ["Psychedelic","Stereo","Progressive"],
    "Year" : 1971,
    "Film" : False,
    "Clip" : True
}

print(dict1.values())

print(dict1.keys())

dict1.update({"Year" : 1973})
print(dict1)

dict1.popitem()
print(dict1)

dict1.pop("Film")
print(dict1)

print(dict1.items())

dict1.setdefault("Number of members", 6)
print(dict1)

print(dict1.get("Genre"))

x = ("key1", "key2", "key3")
y = 0
dict2 = dict.fromkeys(x,y)
print(dict2)

dict3 = dict2.copy()
print(dict3)

dict3.clear()
print(dict3)

