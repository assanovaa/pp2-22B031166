import re
txt = input()
str = '^ab{2,3}'
b = re.search(str,txt)
print (b)