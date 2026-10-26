import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()

    pattern=input("Enter product Name:")
    q=f"Select * from products where productname like '%{pattern}%'"
    smt.execute(q)
    record=smt.fetchall()
    if(record):
        print(record)
    else:
        print("No record found...")
    DB.close()

except Exception as E:
    print("Error:",E)