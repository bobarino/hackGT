import db
import co_api
import time

pl = []
def mainloop():
    ###     MAIN LOOP       ###
    running = True;
    print("Main Loop Running")
    while(running):
        #co_api.updatePurchases();

        userList = db.getUserList()
        purchaseList = db.getPurchaseList()
        pl = db.getPurchaseList()

        #Check for any new purchases for every user

        #iteratively find all of user's transactions, add to ext purchases if not a payout
        for user in userList:
            #Add any new transactions from CO servers
            print(user[14])
            upList = co_api.getPurchases(user[14]).json()
            print(upList)
            for newPurchase in upList:
                    print(newPurchase['_id'])
                    new = True
                    for purchase in purchaseList:
                        print(purchase[5])
                        if(purchase[5] == str(newPurchase['_id'])):
                            #Not a new purchase
                            new = False
                    if(new):
                        db.tabulatePurchase(newPurchase, True)
                        print("New Purchase: ", newPurchase['_id'])

        #Next, see if there are any pending payouts and execute them
        payoutList = db.getPendingPayouts()
        for payout in payoutList:
            #db.execute('UPDATE Payouts(paid) VALUES(%i);',
            #       int(co_api.createPurchase(payout[2], payout[1], payout[3])))
            r = co_api.createPurchase(payout[1],
                                      payout[0],
                                      payout[2])
            if(int(r.json()['code']) == 201):
                db.completePayout(r.json()['objectCreated'])
            else:
                print("Payout could not be completed.")
            
        time.sleep(3)
        running = False

mainloop()
