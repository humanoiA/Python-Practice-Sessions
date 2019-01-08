import sqlite3 as sql
name = input("Enter Name: ")
age=int(input("Enter Age: "))
email=input("Enter E-mail: ")
con = sql.connect("rcpl")
cur=con.cursor()
cur.execute("create table if not exists student(name varchar(30),age int,email varchar(50) primary key)")
cur.execute("insert into student values('{}',{},'{}')".format(name,age,email))
cur.execute("select * from student")
con.commit()
for i in cur.fetchall():
    print(i)
con.close()