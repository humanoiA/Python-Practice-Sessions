l=list()
for i in range(1,52):
    if(i%10==0):
        l.append(str(i))
    else:
        l.append(str(i))
print(l)
while True:
    print("Seats Available are as follows: ")
    for i in range(0,51):
        if(int(l[i])%10==0):
            print(l[i])
        elif int(l[i]==-1):
            print("X",end="\t")
        else:
            print(l[i],end="\t")
    
    num=int(input("Press 0 to exit\nPress 1 to book : "))
    if num==0:
        break
    if num==1:
        num3=int(input("How Many Seats: "))
        if num3<=5:
            for i in range(num3):
                num2=input("Enter Seat Number: ")
                if num2 not in l and int(num2)<51: 
                    print("Seat already Booked")
                elif num2 not in l and int(num2)>=51:
                    print("Out Of Range")
                else:
                    for i in range(0,51):
                        if(l[i]==num2):
                            print("Seat Booked")
                            l[i]=-1
        else:
            print("Max of 5 is Allowed")                    