import pymysql as MYSQL
try:
    DB=MYSQL.connect(host="localhost",user="root",passwd="1234",port=3306,database="pvr")
    smt=DB.cursor()

    mid=input("Enter Movie Id:")
    mn=input("Enter Movie Name:")
    rd=input("Enter Release date:")
    c=input("Enter Cast:")
    d=input("Enter Director:")
    md=input("Enter Music Director:")
 
    s=input("Enter Singers Name:")
    mt=input("Enter Movie type:")
    p=input("Enter ticket price:")
    t=input("Enter Time:")
    po=input("Enter Poster:")

    q=f"Insert into movies values({mid},'{mn}','{rd}','{c}','{md}','{d}','{s}','{mt}',{p},'{t}','{po}')"
    smt.execute(q)
    print(q)

    DB.commit()
    DB.close()
except Exception as E:
    print("Error:",E)