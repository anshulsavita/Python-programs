import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306)
    smt=DB.cursor()
    q="Create Database PVR"
    smt.execute(q)
    print("Database Created Successfully....")
    
    DB.commit()
    DB.close()
except Exception as E:
    print("Error:",E)    