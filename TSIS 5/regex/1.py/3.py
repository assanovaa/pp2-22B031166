import re

txt = input()
str = '[a-z]+_[a-z]+$'
b = re.search(str,txt)
print(b)