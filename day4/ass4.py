print("Enter number of elemnts: ")
num= int(input())
l=list()
for i in range(num):
    l.append(input("Enter Object: "))
if len(l)==0:
    print("list is empty")
else:
    print("list not empty")