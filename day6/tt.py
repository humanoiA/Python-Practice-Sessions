import datetime
file=open('data.txt','w')
mylist=[9012,345345,252,'25dr']
mylist.append(datetime.datetime.now())
#file.write(str(datetime.datetime.now())+',')
#file.write(str(datetime.datetime.now())+',')

file.write(','.join(str(e) for e in mylist))
file.close()