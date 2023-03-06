import re
txt = input()
str = '^a.*b$'
b = re.search(str,txt)
print(b)