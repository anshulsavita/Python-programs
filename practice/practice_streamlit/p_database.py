import pymysql as SQL
def DB_Connect():
    db=SQL.connect(host="localhost",port=3306,user="root",passwd="1234",database="pypractice",cursorclass=SQL.cursors.DictCursor)
    smt=db.cursor()
    return db,smt

def getAllData(query):
    db,smt=DB_Connect()
    smt.execute(query)
    records=smt.fetchall()
    return(records)