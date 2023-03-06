import re
str = input()
txt = '[A-Z][^A-Z]*'
b = re.findall(txt,str)
print(b)