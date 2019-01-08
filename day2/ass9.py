a=int(input("Enter Hardness: "))
b=int(input("Enter Carbon Content: "))
c=int(input("Enter Tensile Strength: "))
if a>50 and b<0.7:
    print("Grade is 9")
elif c>5600 and b<0.7:
    print("Grade is 8")
elif a>50 and c>5600:
    print("Grade is 7")
elif a>50 or b<0.7 or c>5600:
    print("Grade is 6")
else:
    print("Grade is 5")    