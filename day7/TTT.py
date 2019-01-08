print("Welcome to TIc Tac Toe ")
l=[[[" "],[" "],[" "]],    
    [[" "],[" "],[" "]],
    [[" "],[" "],[" "]]]
count=0
while True:
    print(str(l[0])+'\n'+str(l[1])+'\n'+str(l[2]))
    while True:
        print("user 1: ")
        row=int (input("Enter Row No."))
        col = int(input('Enter col no.'))
        if l[row][col]=='X' or l[row][col]=='O':
            print('Select other index ') 
        else:
            l[row][col]='X'
            count=count+1
            break
    print(str(l[0])+'\n'+str(l[1])+'\n'+str(l[2])+'\n\n')
    if l[0][0]==l[0][1]==l[0][2]=='X' or l[1][0]==l[1][1]==l[1][2]=='X' or l[2][0]==l[2][1]==l[2][2]=='X' or l[0][0]==l[1][0]==l[2][0]=='X' or l[0][1]==l[1][1]==l[2][1]=='X' or l[0][2]==l[1][2]==l[2][2]=='X' or l[0][2]==l[1][1]==l[2][0]=='X' or l[0][0]==l[1][1]==l[2][2]=='X' :
        print("user 1 wins")
        break
    if count>8:
        print("Game Tied")
        break
    print(str(l[0])+'\n'+str(l[1])+'\n'+str(l[2])+'\n\n')
    while True:
        print("user 2: ")
        row=int (input("Enter Row No."))
        col = int(input('Enter col no.'))
        if l[row][col]=='X' or l[row][col]=='O':
            print('Select other index ') 
        else:
            l[row][col]='O'
            count=count+1
            break
    if l[0][0]==l[0][1]==l[0][2]=='O' or l[1][0]==l[1][1]==l[1][2]=='O' or l[2][0]==l[2][1]==l[2][2]=='O' or l[0][0]==l[1][0]==l[2][0]=='O' or l[0][1]==l[1][1]==l[2][1]=='O' or l[0][2]==l[1][2]==l[2][2]=='O' or l[0][2]==l[1][1]==l[2][0]=='O' or l[0][0]==l[1][1]==l[2][2]=='O' :
        print("user 2 wins")
        break
    
    

