count=1
for a in range(10,99999):    
    n=len(str(a))
    sum=0
    b=a
    while a!=0:
        rem=a%10
        rem=rem**n
        sum+=rem
        a=int(a/10) 
    if sum == b and count<6:
        print(sum)
        count+=1
    elif count>=6:
        break  
#    if count>=6:
 #       break