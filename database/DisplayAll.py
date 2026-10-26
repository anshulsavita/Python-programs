import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts")
    smt=DB.cursor()

    q="Select * from products"
    smt.execute(q)
    records=smt.fetchall()
    for record in records:
        for col in record:
            print(col,end="\t")
        print()
    DB.close()

except Exception as E:
    print("Error:",E)