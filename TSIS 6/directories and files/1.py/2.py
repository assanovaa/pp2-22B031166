import os
print(os.access(r'C:\Users\001\Desktop\TSIS 6',os.F_OK))
print(os.access(r'C:\Users\001\Desktop\TSIS 6',os.R_OK))
print(os.access(r'C:\Users\001\Desktop\TSIS 6',os.W_OK))
print(os.access(r'C:\Users\001\Desktop\TSIS 6',os.X_OK))