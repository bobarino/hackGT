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
                       purchase['merchant_id'],
                       False,#Payed Out?
                       bool(ext),
                       purchase['_id'])
    cur.execute("""INSERT INTO purchases(amt, account_id, merchant_id, paid, ext, purchase_id)
                        VALUES(%s, %s, %s, %s, %s, %s);""",
                   purchaseColumns)
    con.commit()

def getUserList():
    cur.execute('SELECT * FROM users;')
    return cur.fetchall()
    con.commit()

def getPurchaseList():
    cur.execute('SELECT * FROM purchases;')
    return cur.fetchall()
    con.commit()

def getPendingPayouts():
    cur.execute('SELECT * FROM payouts WHERE paid=FALSE;')
    return cur.fetchall()
    con.commit()

def completePayout(purchase):
    #edit payout to payed and add purchase_id
    print(purchase)
    cur.execute("""UPDATE payouts SET paid=TRUE, purchase_id='%s';""" % str(purchase['_id']))
    print("Payout "+str(purchase['_id'])+" completed.")

    #Add back to purchases to prevent it being seen as an external transaction
    purchaseColumns = (purchase['amount'],
                       purchase['payer_id'],
                       purchase['merchant_id'],
                       True,#Payed Out?
                       False,
                       purchase['_id'])
    cur.execute("""INSERT INTO purchases(amt, account_id, merchant_id, paid, ext, purchase_id)
                        VALUES(%s, %s, %s, %s, %s, %s);""",
                   purchaseColumns)
    con.commit()
