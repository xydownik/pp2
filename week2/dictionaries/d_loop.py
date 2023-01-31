dict1 = {
    "Album" : "The dark side of the moon",
    "Group" : "Pink Floyd",
    "Genre" : ["Psychedelic","Stereo","Progressive"],
    "Year" : 1971,
    "Film" : False,
    "Clip" : True
}
for x in dict1:
    print(dict1[x]) 

for x in dict1.values():
    print(x)
    
for x in dict1.keys():
    print(x)

for x,y in dict1.items():
    print(x,y)