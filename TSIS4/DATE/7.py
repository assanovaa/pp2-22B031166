import datetime
n = datetime.datetime.now()
m = datetime.datetime.now().replace(microsecond=0)
print(n,m,sep="/n")