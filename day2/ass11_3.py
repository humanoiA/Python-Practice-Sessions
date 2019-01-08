for i in range(5,0,-1):
    for j in range(i):
        print(" ",end=" ") 
    for k in range(i,5):
        print("*",end=" ")  
    for l in range(i,4):
        print("*",end=" ")
    print("")
#print(" ",end=" ")
for i,p in zip(range(5),range(4,0,-1)):
    if i==0 and p==4:
        continue
    for j in range(i):
        print(" ",end=" ")
    print(" ",end=" ")
    for k in range(i,3):
        print("*",end=" ")
    for l in range(p):
        print("*",end=" ")
    print(" ")   
     
      
#    print("")        