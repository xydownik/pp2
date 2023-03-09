import os
print('Exist:', os.access('C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/dir_and_files/2f.py ', os.F_OK))
print('Readable:', os.access('C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/dir_and_files/2f.py', os.R_OK))
print('Writable:', os.access('C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/dir_and_files/2f.py', os.W_OK))
print('Executable:', os.access('C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/dir_and_files/2f.py', os.X_OK))