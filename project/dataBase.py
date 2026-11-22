import pymysql as SQL
def DB_connect():
    db=SQL.connect(host='localhost',port=3306,user='root',passwd='1234',database='food',cursorclass=SQL.cursors.DictCursor)
    smt=db.cursor()
    return db,smt

def getAllData(query):
    db,smt=DB_connect()
    smt.execute(query)
    records=smt.fetchall()
    return(records)

def saveRecord(query):
    try:
        db,smt=DB_connect()
        smt.execute(query)
        db.commit()
        db.close()
        return({'status':True,'msg':'Record Submitted'})
    except Exception as e:
        return({'status':False,'msg':e})