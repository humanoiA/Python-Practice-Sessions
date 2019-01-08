print("Enter number of elemnts: ")
num= int(input())
l=list()
for i in range(num):
    l.append(input("Enter Object: "))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            del l[j]
print(l)