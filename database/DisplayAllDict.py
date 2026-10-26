import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()

    q="Select * from products"
    smt.execute(q)
    records=smt.fetchall()
    # print(records)
    for record in records:
        for col in record.values():
            print(col,end='\t')
        # print(record['productname'],record['productrate'])
        print()
    DB.close()

except Exception as E:
    print("Error:",E)