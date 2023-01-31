dict1 = {
    "Album" : "The dark side of the moon",
    "Group" : "Pink Floyd",
    "Genre" : ["Psychedelic","Stereo","Progressive"],
    "Year" : 1971,
    "Film" : False,
    "Clip" : True
}
dict1.pop("Clip")
print(dict1)
dict1.popitem()
print(dict1)
del dict1["Year"]
print(dict1)
dict1.clear()
print(dict1)
del dict1
print(dict1) 