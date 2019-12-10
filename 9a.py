import sqlite3
import os

if(os.path.exists("test.db")):
    os.system("rm test.db")

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

def createStudentDatabase():
    statement = """
    create table student(
    usn varchar(10) primary key,
    name varchar(50),
    age integer,
    address varchar(100))"""
    cursor.execute(statement)
    connection.commit()

def insertStudentValues():
    students = (
        ('1BM17IS063','Rahul Bhaskar',20,'Ashoknagar'),
        ('1BM17ISxxx','xxxxx',20,'xxxx')
    )
    for student in students:
        cursor.execute("insert into student(usn,name,age,address) values(?,?,?,?)",student)
        connection.commit()

def printAllStudent():
    statement = "select * from student"
    cursor.execute(statement)
    students = cursor.fetchall()
    for student in students:
        print(student)

createStudentDatabase()
insertStudentValues()
printAllStudent()