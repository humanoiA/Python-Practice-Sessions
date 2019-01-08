import datetime
file = open("Encrypted.txt","r")
file2 = open('Encrypted2.txt','w')
l=list()
while True:
    try:
        print("1.USE AtM Service")
        print("2.Exit ATM Service")
        n=int(input("Enter Choice: "))
        if n==1:
            try:
                pin=(input("Enter Pin: "))
                for i in file.readlines():
                    st=list(i)
                    del st[(len(st)-1)]
                    dt=''.join(st)
                    mylist=dt.split(',')
                    #print(mylist)
                    if pin == mylist[0]:
                        print("Accesing Account...")
                        print("1.Balance Enquiry")
                        print("2.Withdraw Cash")
                        print("3.Account Information")
                        print("4.Mini Statement")
                #   print("4.Available Balance")
                        choice=int(input('Enter Choice: '))
                        if choice==1:
                            print("Acoount Balance is: ₹",mylist[1])
                        elif choice==2:
                            sum=int(input("Enter Amount to Withdraw: "))
                            #int(mylist[1])
                            mylist[1]=int(mylist[1])-sum
                            print("Available Balance is: ₹",mylist[1])
                            mylist.append(datetime.datetime.now())
                            mylist.append(sum)
                            #file.write(str(datetime.datetime.now())+' '+sum+',')
                        elif choice==3:
                            print("Account Number is: ",mylist[2])
                            print("Accout Holder Name: ",mylist[3])
                       # elif choice==4:
                #   elif choice==4:
            #      print("Available Balance is: ",bal)
                        else:
                            print("Wrong Choice")
                    
                    else:
                        print("Wrong Pin")
                    l=mylist
                    #f.close()  
                    file2.write(','.join(str(e) for e in l))
                    
            except:
                print('Pin can only be digits')
            for j in d.keys():
                for k in range(len(d)):
             #   for l in j[k][1]:
                    if pin == (d[j])[k]:
                        print("Accesing Account...")
                        print("1.Balance Enquiry")
                        print("2.Withdraw Cash")
                        print("3.Account Information")
                        print("4.Mini Statement")
                #   print("4.Available Balance")
                        choice=int(input())
                        if choice==1:
                            print("Acoount Balance is: ₹",(d[j])[1])
                        elif choice==2:
                            sum=int(input("Enter Amount to Withdraw: "))
                            (d[j])[1]-=sum
                            print("Available Balance is: ₹",(d[j])[1])
                        elif choice==3:
                            print("Account Number is: ",(d[j])[0])
                            print("Accout Holder Name: ",(d[j])[2])
                #   elif choice==4:
            #      print("Available Balance is: ",bal)
                        else:
                            print("Wrong Choice")  
                    else:
                        print("Wrong Pin")  
        elif n==2:
            break
        else:
            print("Wrong Choice.")
        
    except:
        print('Only Integer Inputs are supported')
file.close()
file2.close()