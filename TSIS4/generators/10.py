def even_num(n):
    i=0
    while i<n:
        yield i
        i+=2
for i in even_num(int(input())):
    print(i,end=",")