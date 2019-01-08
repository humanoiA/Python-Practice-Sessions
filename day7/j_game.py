import random
print('Welcome to jumble words')
choice=int(input("1.Easy\n2.Medium\n3.Hard:\n"))
if choice==1:
    file = open("jumble1.txt","r")
if choice==2:
    file = open("jumble2.txt","r")
if choice==3:
    file = open("jumble3.txt","r")
for i in file.readlines():
    count=0
    flag=0
    while True:
        
        #i.split('\\n')
        #print(len(i))
        st=list(i)
        del st[(len(st)-1)]
        random.shuffle(st)
        print(''.join(st))
        inw=input("Enter Answer: ")
        inw=inw+'\n'
        if inw==''.join(list(i)):
            print('Right Answer, Moving To Next Question')
            count=1
        if count==1:
            break
        else:
            print('Wrong Answer')
            flag=flag+1
        if flag>2:
            print('Game Over')
            exit()    
file.close()    