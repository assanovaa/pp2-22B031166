import re
txt = input()
str = '^[A-Z][a-z]+'
b = re.search(str,txt)
print(b)