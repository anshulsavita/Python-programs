import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()

    pid=input("Enter product Id:")
    q=f"Select * from products where productid = {pid}"
    smt.execute(q)
    record=smt.fetchone()
    if(record):
        print(record)
    else:
        print(pid,"does not exist...")
    DB.close()

except Exception as E:
    print("Error:",E)