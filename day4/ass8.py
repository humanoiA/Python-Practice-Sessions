print("Enter number of elemnts for list1: ")
num1= int(input())
l1=list()
for i in range(num1):
    l1.append(input("Enter Object: "))
l1.sort()
num=int(input("Enter element to find: "))
if int(l1[len(l1)//2])>num:
    for i in range(0,len(l1)//2):
        if int(l1[i])==num:
            print(i)
if int(l1[len(l1)//2])<num:
    for i in range(len(l1)//2,len(l1)):
        if int(l1[i])==num:
            print(i+1)
if int(l1[len(l1)//2])==num:
    print(i)            