import db
import co_api

running = True;
while(running):
    #Check for any new purchases for every user
    
    #Get list of users
    #db.cur.execute('SELECT * FROM users;')
    userList = []#db.cur.fetchall()

    #iteratively find all of user's transactions, add to ext purchases if not a payout
    for user in userList:
        #Add any new transactions from CO servers
        #upList = getPurchases(user)
	    pass
    running = False
