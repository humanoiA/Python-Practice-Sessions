import re
file = open("file.txt","r")
for i in file:
    words=str(re.split(r',',i)).split(',')
    print("Name is: ",words[0].replace("[",""))