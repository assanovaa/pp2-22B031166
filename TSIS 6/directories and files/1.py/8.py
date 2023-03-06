import os
file_path = os.path.abspath(input())
if os.path.exist(file_path):
    os.remove(file_path)
else:
    print("Can not delete,because this file does not exist")