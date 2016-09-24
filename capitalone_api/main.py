import db
import co_api

###	MAIN LOOP	###
running = True;
while(running):
    co_api.updatePurchases();

    userList = []#db.cur.fetchall()
    purchaseList = []#db.getPurchaseList()

    #Check for any new purchases for every user

    #iteratively find all of user's transactions, add to ext purchases if not a payout
    for user in userList:
	#Add any new transactions from CO servers
	upList = co_api.getPurchases(user[0])
	for newPurchase in upList:
		for purchase in purchaseList:
			if(purchase[6] != newPurchase['_id']):
				#New purchase has been found, create with ext=True
				db.tabulatePurchase(newPurchase, True)

    #Next, see if there are any pending payouts and execute them
    payoutList = db.getPendingPayouts()
    for payout in payoutList:
	db.execute('UPDATE Payouts(paid) VALUES(%i);',
		int(co_api.createPurchase(payout[2], payout[1], payout[3]))
)
    running = False
