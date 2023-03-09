import os
print("Test a path exists or not:")
path = r'C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/dir_and_files/2f.py'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))