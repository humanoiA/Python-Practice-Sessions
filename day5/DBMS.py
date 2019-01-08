import os
d=dict()
l=list()
while True:
    l=[]
    print("1.Insert Student Record.")
    print("2.Display Record.")
    print("3.Delete Record.")
    print("4.Edit Student Record.")
    print("5.Exit.")
    num=int(input())
    if num not in range(1,6):
        print("Wrong Choice")
    if num==5:
        break
    if num==1:
        id=int(input("Enter Id: "))
        name=(input("Enter Name: "))
        l.append(name)
        for i in range(1,5):
            l.append(int(input("Enter marks for subject : ")))
        d[id]=l
        del l
    if num==2:
        print("1.Display All Record.")
        print("2.Display By Id.")
        print("3.Display By Name.")
        num2=int(input("Enter Choice: "))
        if num2==1:
            print(d)
        if num2==2:
            id1=int(input("Enter id: "))
            print(d[id1])
        if num2==3:
            name=input("Enter name: ")
            for i in d.items():
                if name in i[1]:
                    print((i[1])[1:5])    
        if num2 not in range(1,4):
            print("Wrong Choice")
    if num==3:
        print("1.Delete All Record.")
        print("2.Delete By Id.")
        num3=int(input("Enter Choice: "))
        if num3==1:
            d.clear()
        if num3==2:
            id2=int(input("Enter id: "))
            d.pop(id2)    
        if num3 not in range(1,3):
            print("Wrong Choice")
    if num==4:
        print("1.Edit Student Record.")
        num4=int(input("Enter Choice: "))
        if num4==1:
            num5=int(input("Enter id to edit: "))
            print("1. Edit Name")
            print("2. Edit Marks")
            num6=int(input("Enter Choice: "))
            if num6==1:
                (d[num5])[0]=input("Enter Name:")
            if num6==2:
                (d[num5])[1]=input("Enter Marks:")
                (d[num5])[2]=input("Enter Marks:")
                (d[num5])[3]=input("Enter Marks:")
                (d[num5])[4]=input("Enter Marks:")
        if num5!=1:
            print("Wrong Choice")

                

            
                    
   