import re
file = open("file.txt","r")
for i in file.readlines():
    print(i.split(','))
file.close()