import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts")
    smt=DB.cursor()

    pid=input("Enter product Id:")
    pn=input("Enter product Name:")
    pr=input("Enter product Rate:")
    po=input("Enter product Offer:")
    pd=input("Enter product M. Date:")

    q=f"Insert into products values({pid},'{pn}',{pr},{po},'{pd}')"
    smt.execute(q)
    print(q)

    DB.commit()
    DB.close()
except Exception as E:
    print("Error:",E)