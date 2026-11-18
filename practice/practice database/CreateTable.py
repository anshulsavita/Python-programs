import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="pvr")
    smt=DB.cursor()
    q="Create table Movies(Movieid int primary key,Moviename varchar(50) not null,releasedate date not null,cast varchar(100) not null,music_director varchar(50) not null,director varchar(50) not null,singers varchar(40) null, movie_type varchar(50) not null,price decimal(8,2) not null,time varchar(50) not null,poster varchar(50) not null)"

    smt.execute(q)
    print("Table Created Successfully....")

    DB.commit()
    DB.close()

except Exception as E:
    print("Error:",E)