import os
path = "C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/junk.txt"
res = os.path.join(path)
if os.access(path, os.F_OK):
    print("Exists, ready to delete")
    os.remove(res)
else:
    print("Doesn't exist")
