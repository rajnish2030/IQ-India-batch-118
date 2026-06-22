# import pymysql

# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="203020",
# )
# print("Database Connected Successfully")

# target = ["DB1","DB2","DB3"]
# import pymysql
# mysql_connection =pymysql.connect(
#     user="root",
#     host="localhost",
#     passwd="203020"
#     )
# agent = mysql_connection.cursor()
# for i in target:
#     agent.execute(f"create database {i}")
#     agent.execute("Show database")
#     for db in agent.fetchall():
#         print(db)
#         mysql_connection.close()
#---------------------------------#
# target = ["DB1", "DB2", "DB3"]

# import pymysql

# mysql_connection = pymysql.connect(
#     user="root",
#     host="localhost",
#     passwd="203020"
# )

# agent = mysql_connection.cursor()

# for i in target:
#     agent.execute(f"CREATE DATABASE IF NOT EXISTS {i}")

# agent.execute("SHOW DATABASES")

# for db in agent.fetchall():
#     print(db)

# mysql_connection.close()

#1.ask user for db-name
#2.ask user for table-name
#3.name,age,address
#4.store in database using pyhton-connectivity

import pymysql
db_name = input("Enter Database Name: ")
table_name = input("Enter Table Name: ")
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="203020")
cur = conn.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cur.execute(f"USE {db_name}")

cur.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name}(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    address VARCHAR(100))""")
name = input("Enter Name: ")
age = int(input("Enter Age: "))
address = input("Enter Address: ")
sql = f"INSERT INTO {table_name}(name, age, address) VALUES(%s, %s, %s)"
cur.execute(sql, (name, age, address))
conn.commit()
print("Data Stored Successfully!")
conn.close()


# #connect db with function
# import pymysql
# from tabulate import tabulate
# def db_connect(host,user,password,database):
#     conn = pymysql.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )
#     agent = conn.cursor()
#     agent.execute("select * from student_data")
#     row = agent.fetchall()
#     print(tabulate(row))
# db_connect(user="root",host="localhost",password="203020",database="student_management")
# #     return conn

# # conn = db_connect()

# # if conn:
# #     cur = conn.cursor()
# #     cur.execute("SELECT * FROM student_data")  
# #     data = cur.fetchall()
# #     print("Table Data:")
# #     for row in data:
# #         print(row)
# #     cur.close()
# #     conn.close()

# # #wap a program len of list
# # cities=["Bihar","Delhi","Noida","Delhi"]
# # number =[1,2,3,4,5]
# # print(len(cities))
# # print(len(number))

# # def print_list(list):
# #     for i in list:
# #         print(list,end="")
# # print(cities)


# def connect_to_db(user,host,password):
#     mysql_connection = pymysql.connect(user=user,host=host,password=password)
#     return mysql_connection
# connect_to_db(user="root",host="localhost",password="203020")

# import pymysql

# def connect_to_db(user, host, password):
#     mysql_connection = pymysql.connect(
#         user=user,
#         host=host,
#         password=password
#     )
#     return mysql_connection


# def create_db(db_name):
#     conn = connect_to_db(
#         user="root",
#         host="localhost",
#         password="203020"
#     )
#     cursor = conn.cursor()
#     cursor.execute(f"CREATE DATABASE {db_name}")
#     conn.commit()
#     print("Database Created Successfully")
#     cursor.execute("SHOW DATABASES")
#     for db in cursor.fetchall():
#         print(db[0])
#     cursor.close()
#     conn.close()
# db_name = input("Enter Your DB Name: ")
# create_db(db_name)

# #---------------------------------------
# def connect_to_db(user,host,password):
#     mysql_connection = pymysql.connect(user=user,host=host,password=password)
#     return mysql_connection
# connect_to_db(user="root",host="localhost",password="203020")


# #----------------------------------------------------------------------

# def create_db(db_name):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     cursor.execute(f"CREATE DATABASE {db_name}")
#     print("Database Created Successfully")
#     cursor.execute("SHOW DATABASES")
#     for db in cursor.fetchall():
#         print(db[0])
#     cursor.close()
#     conn.close()
# db_name = input("Enter Your DB Name: ")
# create_db(db_name)

# #---------------------------------------------------
# import pymysql

# def create_database(db_name):
#     conn = pymysql.connect(
#         host="localhost",
#         user="root",
#         password="203020"
#     )
#     cur = conn.cursor()
#     cur.execute(f"CREATE DATABASE {db_name}")
#     print("Database Created Successfully")
#     cur.close()
#     conn.close()
# db_name = input("Enter Database Name: ")
# create_database(db_name)


# create a databse 
#-------Connect database ----------
import pymysql
def connect_to_db(user,host,password):
    mysql_connection = pymysql.connect(
        user=user,
        host=host,
        password=password
    )
    return mysql_connection

connect_to_db(user="root",host="localhost",password="203020")

# # after this 
# # ------------ Create Database -----------
def create_database(db_name):
    conn = connect_to_db("root", "localhost", "203020")
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {db_name}")
    print("Database Created Successfully")
    cur.close()
    conn.close()
db_name = input("Enter Database Name: ")
create_database(db_name)

#--------------show database ------------------
def show_databases():
    conn = connect_to_db("root", "localhost", "203020")
    cur = conn.cursor()
    cur.execute("SHOW DATABASES")
    for db in cur.fetchall():
        print(db[0])
    cur.close()
    conn.close()
show_databases()


#-------------------------------------
#-----create table ----------
import pymysql
def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="203020",
        database="student_management"
    )
def create_table():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE student(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50),
        age INT,
        salary int
        )
    """)
    print("Table Created Successfully")
    cur.close()
    conn.close()
create_table()



# database connection --with pyhton-----
import pymysql
def my_db(data_list):
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="203020"
    )
    cursor = db.cursor()
    for i in data_list:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {i}")
        print(f"{i} checked/created")
    db.close()
target_db_name = ['staff', 'student', 'employees']
my_db(target_db_name)
