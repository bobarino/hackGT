import psycopg2
import json
import co_api
import dbinfo

con = psycopg2.connect(database=dbinfo.name, user=dbinfo.user, password=dbinfo.password)
cur = con.cursor()

def execSQL(command):
    cur.execute(str(command))
    result = cur.fetchall()
    print(result)

#execSQL('SELECT * FROM testTable;')

def tabulatePurchase(purchase, ext):
    purchaseColumns = (purchase['amount'],
                       purchase['payer_id'],
                       purchase['payee_id'],
                       purchase['purchase_date'],
                       false,#Payed Out?
                       bool(ext))
    db.cur.execute("""INSERT INTO CO_Purchases(amount, account_id, merchant_id, date, payed, ext)
                        VALUES(%s, %s, %s, %s, %s, %s);""",
                   purchaseColumns)

def getUserList():
    db.cur.execute('SELECT * FROM Users;')
    return db.cur.fetchall()

def getPurchaseList():
    db.cur.execute('SELECT * FROM CO_Purchases;')
    return db.cur.fetchall()

def getPendingPayouts():
    db.cur.execute('SELECT * FROM Payouts WHERE paid=FALSE;')
    return db.cur.fetchall()

def 
