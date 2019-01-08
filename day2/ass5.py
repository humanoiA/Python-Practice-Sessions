a = int(input("Enter number: "))
if a>10000 and a<=99999:
    sum=0
    b=a
    sum+=a%10
    a=int(a/10)
    sum=sum*10+a%10
    a=int(a/10)
    sum=sum*10+a%10
    a=int(a/10)
    sum=sum*10+a%10
    a=int(a/10)
    sum=sum*10+a%10
    print(sum)
    if sum == b:
        print("Original Number")
    else:
        print("Not Original")    