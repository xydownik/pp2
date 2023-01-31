dict1 = {
    "Album" : "The dark side of the moon",
    "Group" : "Pink Floyd",
    "Genre" : ["Psychedelic","Stereo","Progressive"],
    "Year" : 1971,
    "Film" : False,
    "Clip" : True
}

print(dict1["Clip"])

x= dict1.get("Genre")
print(x)

x= dict1.keys()
print(x)

dict1["Design"] = "Storm Thorgerson"
print(x)

y = dict1.values()
print(y)

dict1["Film"] = True
print(y)

z= dict1.items()
print(z)

if "Design" in dict1:
    print("Exists")
    
