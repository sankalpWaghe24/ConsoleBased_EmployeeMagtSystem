import mysql.connector as mysql

conn = mysql.connect(user='root', password='', host='localhost')
cursor = conn.cursor()
q = "use sankalpdb"  # go to database
cursor.execute(q)
# print("Great Success")


# Insert table


def savedata():
    a = input("Enter Employee Name : ")
    b = eval(input("Enter Employee Salary : "))
    c = input("Enter Employee Contact : ")

    q1 = "insert into emp_data(name,salary,contact) values( '"+a+"','"+str(b)+"','"+c+"' ) "
    cursor.execute(q1)
    conn.commit()
    print("Great Success")

# savedata()


def fetchdata():
    q2 = "Select * from emp_data "
    cursor.execute(q2)
    res = cursor.fetchall()
    for i in res:
        print(i)
    print("Great Success")

# fetchdata()


def del_data():
    a = input("Enter Employee ID : ")

    q3 = " delete from emp_data where id='"+a+"' "
    cursor.execute(q3)
    conn.commit()
    print("Great Success")
# del_data()


def update_data():
    a = input("Enter Employee name : ")
    b = input("Enter Employee ID : ")
    q4 = "update emp_data set name= '"+b+"' where id='"+a+"' "
    cursor.execute(q4)
    conn.commit()
    print("Great Success")
# update_data()


def search_data():
    a = input("Enter Employee ID : ")
    q5 = "select * from emp_data where id='"+a+"' "
    cursor.execute(q5)
    res = cursor.fetchone()
    print(res)
    print("Great Success")

# search_data()


def search_data():
    a = input("Enter Employee Highest : ")
    q5 = "select * from emp_data where id='"+a+"' "
    cursor.execute(q5)
    res = cursor.fetchall()
    print(res)
    print("Great Success")


search_data()