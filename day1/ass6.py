a=int(input("Enter 3 digit number: "))
sum=0
sum+=a%10
a=int(a/10)
sum+=a%10
a=int(a/10)
sum+=a%10
print(sum)