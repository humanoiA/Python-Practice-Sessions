print("Enter number of elemnts: ")
num= int(input())
l=list()
for i in range(num):
    l.append(input("Enter Object: "))
flag = int(input("Enter 1 for addition and 2 for multiplication: "))
times=int(input("Enter number of iterations: "))
if flag==1:
    for i in range(times):
        l.append(input("Enter Object: "))
elif flag==2:
    l=l*times
print(l)
        