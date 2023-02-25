def gensquares(n):
    for i in range(n):
        yield i**2
        i+=1
for i in gensquares(int(input())):
    print(i)
