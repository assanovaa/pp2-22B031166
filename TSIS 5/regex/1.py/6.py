import re 
txt ='[ ,.]'
m = input()
str = re.sub(txt,':',m)
print(str)