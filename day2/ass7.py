a = int(input("Enter number: "))
n=len(str(a))
sum=0
b=a
while a!=0:
    rem=a%10
    rem=rem**n
    sum+=rem
    a=int(a/10)
if sum == b:
    print("Armstrong Number")
else:
    print("Not Armstrong")    