import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()

    min=input("Enter min price:")
    max=input("Enter max price:")
    q=f"Select * from products where productrate between {min} and {max}"
    smt.execute(q)
    record=smt.fetchall()
    if(record):
        print(record)
    else:
        print("No record found...")
    DB.close()

except Exception as E:
    print("Error:",E)