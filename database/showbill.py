import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="lgproducts",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()
    pn="products"
    pr="Rate"
    po="Offer"
    bn=input("Enter Bill no:")
    q=f"SELECT * FROM bill,sales,products where sales.billno=bill.billno and products.productid=sales.productid and bill.billno={bn}"
    smt.execute(q)
    records=smt.fetchall()
    # print(records)
    if(len(records)!=0):
        print("\t\t\t\tInvoice")
        print(f"\t\tDate:{records[0]['billdate']}")
        print(f"\t\tBillno:{records[0]['billno']}")
        print(f"\t\tCustomer:{records[0]['customername']}")
        print(f"\t\tPayment type:{records[0]['paymentmode']}")
        print("\t\t----------------------------------------------------------------------------------------")
        print(f"\t\tSN\t{pn:<20}\t{pr:<12}\t{po:<12}\tQty\tAmount")
        print("\t\t----------------------------------------------------------------------------------------")
        for i,record in enumerate(records):
            print(f"\t\t{i+1}\t{record['productname']:<20}\t{record['productrate']:<12}\t{record['offer']:<12}\t{record['qty']}\t{record['qty']*record['offer']}")
       
    else:
        print(bn,"does not exist...")
    DB.close()

except Exception as E:
    print("Error:",E)


# city
# cityid
# cityname
# 
#  screen
# cityid fk
# screenid pk
# screenname 

# movie
# cityid

# input cityid