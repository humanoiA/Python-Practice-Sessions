size=int(input())
number=int(input())
rem=number
sum1=0
sum2=0
for i in range(1,size//2):
    rem=rem%10
    if rem==4 or rem==7:
        sum1+=rem
    else:
        print('NO')
        exit(1)
    rem=int(rem/10)
for j in range(size//2,size+1):
    rem=rem%10
    if rem==4 or rem==7:
        sum2+=rem
    else:
        print('NO')
        exit(1)
    rem=int(rem/10)
print(sum1,sum2)