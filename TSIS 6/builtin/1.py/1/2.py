s=input()
count=0
count1=0
for x in s:
        if x.isupper():
            count+=1
        else:
            count1+=1


print(count,count1)