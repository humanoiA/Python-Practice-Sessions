a=int(input("Enter 5 digit number: "))
if a>=10000 and a<=99999:
    sum=0
    while a!=0:
        sum+=a%10
        a=int(a/10)
    print(sum)
else:
    print("not 5 digit number")    