import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="pvr",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()
    cityid=input("Enter city ID:")
    q=f"SELECT * FROM city inner join movies on movies.cityid=city.cityid inner join screen on screen.cityid=city.cityid where city.cityid={cityid}"
    smt.execute(q)
    records=smt.fetchall()
    if(len(records)!=0):
        print("\t\t\t\tInvoice")
        print(f"\t\tMovie Id:{records[0]['Movieid']}")
        print(f"\t\tMovie Name:{records[0]['Moviename']}")
        print(f"\t\tCity ID:{records[0]['cityid']}")
        print(f"\t\tCity Name:{records[0]['cityname']}")
        print(f"\t\tScreen ID:{records[0]['screenid']}")
        print(f"\t\tScreen Name:{records[0]['screenname']}")
        print("\t\t----------------------------------------------------------------------------------------")
        print(f"\t\tSN\tMovie ID\tMovie Name\tCity ID\tCity Name\tScreen ID\tScreen Name")
        print("\t\t----------------------------------------------------------------------------------------")
        for i,record in enumerate(records):
            print(f"\t\t{i+1}\t{record['Movieid']}\t\t{record['Moviename']}\t{record['cityid']}\t{record['cityname']}\t\t{record['screenid']}\t\t{record['screenname']}")
    
    else:
        print(cityid,"does not exist...")
    DB.close()

except Exception as E:
    print("Error:",E)
