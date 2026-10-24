import pymysql as MYSQL
# try use for prevent crash and print error carefully
try:
# login, Imagine DB as homescreen in mysql after providing password or after login screen.
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306)

# this is for have mysql curser, smt is a cursor
    smt=DB.cursor()

# query to create databse
    q="Create Database LGProducts"

# give query to cursor
    smt.execute(q)
    print("Database Created Successfully....")

    DB.commit()
    DB.close()

# Handles the exception if an error occurs in the try block.
except Exception as E:
    print("Error:",E)