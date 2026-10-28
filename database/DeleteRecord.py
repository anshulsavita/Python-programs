import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()
    pid=input("Enter Product Id u want to Delete:")
    q=f"select * from products where productid={pid}"
    smt.execute(q)
    record=smt.fetchone()
    if(record):
        print('Id:',record['productid'],)
        print('Name:',record['productname'],)
        print('Rate:',record['productrate'],)
        print('offer:',record['offer'],)
        ch=input("Are u sure to delete the above record [yes/no]?:")
        if(ch.lower()=="yes"):
            q=f"delete from products where productid={pid}"
            smt.execute(q)
            DB.commit()
            print(record["productname"],"Deleted Successfully")
        else:
            print("Product Not Removed")
    else:
        print("Record not found..")
    DB.close()

except Exception as E:
    print("Error:",E)