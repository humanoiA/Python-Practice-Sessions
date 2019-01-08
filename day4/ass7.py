print("Enter number of elemnts for list1: ")
num1= int(input())
l1=list()
l2=list()
for i in range(num1):
    l1.append(input("Enter Object: "))
n=int(input("Enter the value of n"))
for i in range(n):
    for j in range(len(l1)):
        l2.append(l1[j]+str(int(i+1)))
print(l2)
