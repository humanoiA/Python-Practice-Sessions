print("Enter number of elemnts for list1: ")
num1= int(input())
l1=list()
for i in range(num1):
    l1.append(input("Enter Object: "))
print("Enter number of elemnts for list 2: ")
num2= int(input())
l2=list()
for i in range(num2):
    l2.append(input("Enter Object: "))
for i in range(num2):
    l1.append(l2[i])
print("Appended list is : ")
print(l1)
