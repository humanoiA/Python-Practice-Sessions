print("Enter number of elemnts: ")
num= int(input())
l=list()
count=0
for i in range(num):
    l.append(input("Enter Object: "))
for i in range(num):
    if len(l[i])>2:
        if (l[i])[-1]==(l[i])[0]:
            count=count+1
    else:
        continue
print(count)        