import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="pvr",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()
    mid=input("Enter Movie Id u want to Delete:")
    q=f"SELECT * FROM movies where movieid={mid}"
    smt.execute(q)
    record=smt.fetchone()

    if(record):
        print('Id:',record['Movieid'],)
        print('Name:',record['Moviename'])
        print('Release Date:',record['releasedate'])
        print('Cast:',record['cast'])
        ch=input("Are u sure to delete the above record [yes/no]?:")
        if(ch.lower()=="yes"):
            q=f"delete from movies where movieid={mid}"
            smt.execute(q)
            DB.commit()
            print(record["Moviename"],"Deleted Successfully")
        else:
            print("Movie Not Removed")
    else:
        print("Record not found..")
    DB.close()

except Exception as E:
    print("Error:",E)