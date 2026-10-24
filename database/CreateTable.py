import pymysql as MYSQL
# try use for prevent crash and print error carefully
try:
# login, Imagine DB as homescreen in mysql after providing password or after login screen.
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts")

# this is for have mysql curser, smt is a cursor
    smt=DB.cursor()

# query to create table
    q="Create table products(productid int primary key,productname varchar(20) not null,productrate decimal(10,2) not null, offer decimal(10,2),mdate date)"

# give query to cursor
    smt.execute(q)
    print("Table Created Successfully....")

    DB.commit()
    DB.close()

# Handles the exception if an error occurs in the try block.
except Exception as E:
    print("Error:",E)