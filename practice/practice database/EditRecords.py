import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="pvr",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()
    mid=input("Enter Movie Id u want to Edit:")
    q=f"select * from movies where movieid={mid}"
    smt.execute(q)
    record=smt.fetchone()

    if(record):
        print(' Movie Id:',record['Movieid'])
        print('1]Movie Name:',record['Moviename'])
        print('2]Release date:',record['releasedate'])
        print('3]Cast:',record['cast'])
        print('4]Ticket Price:',record['price'])
        print('5]Show timing:',record['time'])
        print('6]Exit')

        ch=int(input("Are ur choise:"))
        pat=None
        if(ch==1):
            nn=input("Enter New Name:")
            pat=f"moviename='{nn}'"
        elif(ch==2):
            nrd=input("Enter New Release date:")
            pat=f"releasedate={nrd}"
        elif(ch==3):
            nc=input("Enter New Cast:")
            pat=f"cast={nc}"
        elif(ch==4):
            np=input("Enter New Ticket Price:")
            pat=f"price='{np}'"
        elif(ch==5):
            nt=input("Enter New Show timing:")
            pat=f"time='{nt}'"
        elif(ch==6):
            print("Exit Good Bye")
        else:
            print("Wrong Option")
        if(pat!=None):
            q=f"update movies set {pat} where movieid={mid}"
            smt.execute(q)
            DB.commit()
            print("Record Updated Successfully...")
    else:
        print("Record not found...")

    DB.close()

except Exception as E:
    print("Error:",E)