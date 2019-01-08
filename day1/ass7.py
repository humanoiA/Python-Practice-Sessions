a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))
if(a>b):
    if(b>c):
        print(b)
    else:
        print(c)
else:
    if(a>c):
        print(a)
    else:
        print(c)