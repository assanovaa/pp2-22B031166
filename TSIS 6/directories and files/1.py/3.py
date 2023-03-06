import os
o = r'C:\Users\001\Desktop\TSIS 6\Directories and Files'
if os.path.exists(o):
    basename= os.path.basename(o)
    path_dir = os.path.dirname(o)
    print(basename)
    print(path_dir)
else:
    print("Does not exist")
