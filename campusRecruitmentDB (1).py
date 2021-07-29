#importing module
import mysql.connector

#establishing connection with server
mydb=mysql.connector.connect(host='localhost',user='root',password='root',buffered=True)

#creating cursor
mycursor = mydb.cursor()

#creating database
#create_db = "CREATE DATABASE CampusRecruitment"
#mycursor.execute(create_db)

#connecting to database
mycursor.execute("USE CampusRecruitment")

#creating tables
'''create_tb1 = """CREATE TABLE student
(student_id int NOT NULL,
name varchar(225),
email varchar(225),
phone_no int NULL,
gender char(20),
department char(40),
ssc_percent float(4,2),
ssc_board char(40),
hsc_percent float(4,2),
hsc_board char(40),
degree_percent float(4,2),
apti_percent float(4,2),
work_exp char(20),
placement_status char(20),
salary int NULL,
company varchar(225) NULL
)"""
mycursor.execute(create_tb1)'''
 
'''create_tb2= """CREATE TABLE company
(company_id int not null,
name varchar(225),
address varchar(225)
)"""
mycursor.execute(create_tb2)'''

'''create_tb3= """CREATE TABLE jobposting
(job_id int,
name varchar(225),
company varchar(225),
salary int,
min_aptiPercent decimal(4,2),
min_bePercent decimal(4,2),
min_workExp char(20)
)"""
mycursor.execute(create_tb3)'''

#inserting values in student table
def std_values(val):
    query = """INSERT INTO student(student_id,name,email,phone_no,gender,department,ssc_percent,ssc_board,hsc_percent,hsc_board,degree_percent,apti_percent,work_exp,placement_status,salary,company)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(query,val)
    mydb.commit()

#inserting values in jobposting table
def app_values(val):
    query = """INSERT INTO jobposting(job_id,name,company,salary,min_aptiPercent,min_bePercent,min_workExp)
    VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(query,val)
    mydb.commit()

#inserting values in company table
def com_values(val):
    query = """INSERT INTO company(company_id,name,address)
    VALUES(%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()

#view student profile
def std_view(val):
    query = "SELECT * FROM student WHERE student_id = " + val
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result

#view admin profile
def ad_view(val):
    query = "SELECT * FROM jobposting WHERE job_id = " + val
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result
    
#view company profile
def com_view(val):
    query = "SELECT * FROM company WHERE company_id = " + val
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result
    
#delete record from student
def std_del(val):
    query = "DELETE FROM student WHERE student_id = " + val
    mycursor.execute(query)
    mydb.commit()

#delete record from company
def com_del(val):
    query = "DELETE FROM company WHERE company_id = " + val
    mycursor.execute(query)
    mydb.commit()
    
#delete record from jobposting
def ad_del(val):
    query = "DELETE FROM jobposting WHERE job_id = " + val
    mycursor.execute(query)
    mydb.commit()
    
    
