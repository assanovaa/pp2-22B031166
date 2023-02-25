from datetime import datetime,time
n=datetime.now()
m=datetime.strptime('2021-01-01 02:02:03','%Y-%m-%d %H:%M:%S')
a=(n-m).seconds
print(a)