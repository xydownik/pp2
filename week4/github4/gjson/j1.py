import json
with open('file.json', 'r') as f:
    data = json.load(f)
print("Interface status")
print("DN", " " * 47, "Description"," "*10, "Speed", " "*1, "MTU")
print("-"*50, "-"*20,"-"*6," "*1, "-*6")
for interface in data["imdata"]:
    for i in interface:
        for j in interface[i]:
            print(interface[i][j]["dn"],"\t"*4,interface[i][j]["mtu"])