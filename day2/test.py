for i,p in zip(range(5),range(4,0,-1)):
    for j in range(i):
        print(" ",end=" ")
    for k in range(i,3):
        print("*",end=" ")
    for l in range(p):
        print("*",end=" ")
    
    
    print("")   