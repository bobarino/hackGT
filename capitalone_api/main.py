import db
import co_api

###     MAIN LOOP       ###
running = True;
print("Main Loop Running")
while(running):
    #co_api.updatePurchases();

    userList = db.getUserList()
    purchaseList = db.getPurchaseList()

    #Check for any new purchases for every user

    #iteratively find all of user's transactions, add to ext purchases if not a payout
    for user in userList:
        #Add any new transactions from CO servers
        upList = co_api.getPurchases(user[3]).json()
        print(upList, '\n')
        for newPurchase in upList:
                print(newPurchase['_id'], '\n')
                new = True
                for purchase in purchaseList:
                    print(purchase[3], '\n')
                    if(purchase[3] == str(newPurchase['_id'])):
                        #Not a new purchase
                        new = False
                if(new):
                    db.tabulatePurchase(newPurchase, True)
                    print("New Purchase: ", newPurchase['_id'])

    #Next, see if there are any pending payouts and execute them
    #payoutList = db.getPendingPayouts()
    #for payout in payoutList:
        #db.execute('UPDATE Payouts(paid) VALUES(%i);',
        #       int(co_api.createPurchase(payout[2], payout[1], payout[3]))
#)
    #running = False
