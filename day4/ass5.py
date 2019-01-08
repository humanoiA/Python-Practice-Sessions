print("Enter number of elemnts: ")
num= int(input())
str=''
l=list()
for i in range(num):
    l.append(input("Enter characters: "))
for i in range(len(l)):
    str+=l[i]
print(str)
