import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()
    pid=input("Enter Product Id u want to Edit:")
    q=f"select * from products where productid={pid}"
    smt.execute(q)
    record=smt.fetchone()
    if(record):
        print('Id:',record['productid'])
        print('1]Name:',record['productname'])
        print('2]Rate:',record['productrate'])
        print('3]offer:',record['offer'])
        print('4]Md Date:',record['mdate'])
        print('5]Exit')

        ch=int(input("Are ur choise:"))
        pat=None
        if(ch==1):
            nn=input("Enter New Name:")
            pat=f"productname='{nn}'"
        elif(ch==2):
            nr=input("Enter New Rate:")
            pat=f"productrate={nr}"
        elif(ch==3):
            no=input("Enter New Offer:")
            pat=f"offer={no}"
        elif(ch==4):
            nd=input("Enter New M.Date:")
            pat=f"mdate='{nd}'"
        elif(ch==5):
            print("Exit Good Bye")
        else:
            print("Wrong Option")
        if(pat!=None):
            q=f"update products set {pat} where productid={pid}"
            smt.execute(q)
            DB.commit()
            print("Product Updated Successfully...")

    DB.close()

except Exception as E:
    print("Error:",E)