import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="pvr",cursorclass=MYSQL.cursors.DictCursor)
    smt=DB.cursor()

    q=False
    print("------Main Menu-----")
    print("1.Id\n2.Name\n3.cast\n4.Director\n5.Movie Type\n")
    ch=int(input("Enter How u want to Search:"))

    match ch:
        case 1:
            id=input("Enter Movie Id:")
            q=f"Select * from movies where movieid = {id}"
        
        case 2:
            name=input("Enter Movie Name:")
            q=f"Select * from movies where moviename like '%{name}%'"
        

        case 3:
            cast=input("Enter Movie's cast:")
            q=f"Select * from movies where cast like '%{cast}%'"
        
        case 4:
            dir=input("Enter Movie's Director:")
            q=f"Select * from movies where director like '%{dir}%'"
        
        case 5:
            mt=input("Enter Movie type:")
            q=f"Select * from movies where movie_type like '%{mt}%'" 
        
        case _:
            print("Wrong input...")

    if(q):
        smt.execute(q)
        record=smt.fetchall()
        if(record):
            print(record)
        else:
            print("does not exist...")
    DB.close()

except Exception as E:
    print("Error:",E)