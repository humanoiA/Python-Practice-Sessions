import sqlite3 as sql
con = sql.connect("stud_dbms")
cur=con.cursor()
while True:
    print("1.Insert Student Record.")
    print("2.Display Record.")
    print("3.Delete Record.")
    print("4.Edit Student Record.")
    print("5.Exit.")
    num=int(input())
    if num not in range(1,6):
        print("Wrong Choice")
    if num==5:
        break
    if num==1:
        id=int(input("Enter Student id: "))
        name = input("Enter Name: ")
        age=int(input("Enter Age: "))
        gender=input("Enter gender: ")
        email=input("Enter E-mail: ")
        address=input("Enter address: ")
        cur.execute("create table if not exists student(id int primary key,name varchar(30),age int,gender varchar(6),email varchar(50),address varchar(100))")
        cur.execute("insert into student values({},'{}',{},'{}','{}','{}')".format(id,name,age,gender,email,address))
        con.commit()

    if num==2:
        print("1.Display All Record.")
        print("2.Display By Id.")
        print("3.Display By Name.")
        num2=int(input("Enter Choice: "))
        if num2==1:
            count=0
            cur.execute("select * from student")
            con.commit()
            for i in cur.fetchall():
                count=count+1
            if count==0:
                print('No record found')
            cur.execute("select * from student")
            con.commit()
            if count!=0:
                print('ID','\t','NAME','\t','AGE','\t','GENDER','\t','EMAIL','\t','ADDRESS','\t')
                for i in cur.fetchall():
                    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t')
        if num2==2:
            id1=int(input("Enter id: "))
            cur.execute("select * from student where id = {}".format(id1))
            con.commit()
            print('ID','\t','NAME','\t','AGE','\t','GENDER','\t','EMAIL','\t','ADDRESS','\t')
            for i in cur.fetchall():
                print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t')
        if num2==3:
            name=input("Enter name: ")
            cur.execute("select * from student where name = '{}'".format(name))
            con.commit()
            print('ID','\t','NAME','\t','AGE','\t','GENDER','\t','EMAIL','\t','ADDRESS','\t')
            for i in cur.fetchall():
                print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t')
        if num2 not in range(1,4):
            print("Wrong Choice")
    if num==3:
        print("1.Delete All Record.")
        print("2.Delete By Id.")
        num3=int(input("Enter Choice: "))
        if num3==1:
            cur.execute("delete from student ")
            con.commit()
        if num3==2:
            id1=int(input("Enter id: "))
            cur.execute("delete from student where id = {}".format(id1))
            con.commit()
        if num3 not in range(1,3):
            print("Wrong Choice")
    if num==4:
        print("1.Edit Student Record.")
        num4=int(input("Enter Choice: "))
        if num4==1:
            id=int(input("Enter Student id: "))
            name = input("Enter Name: ")
            age=int(input("Enter Age: "))
            gender=input("Enter gender: ")
            email=input("Enter E-mail: ")
            address=input("Enter address: ")
            cur.execute("update student set name='{}',age={},gender='{}',email='{}',address='{}' where id = {}".format(name,age,gender,email,address,id))
            con.commit()
        else:
            print("Wrong Choice")
con.close()