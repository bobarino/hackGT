import db
import co_api
import time

pl = []
def mainloop():
    ###     MAIN LOOP       ###
    running = True;
    print("Main Loop Running")
    while(running):
        userList = db.getUserList()
        purchaseList = db.getPurchaseList()
        pl = db.getPurchaseList()

        #Check for any new purchases for every user
        print("Checking for new transactions...")
        #iteratively find all users' transactions, add to (ext) purchases if not there
        for user in userList:
            #Add any new transactions from CO servers
            upList = co_api.getPurchases(user[14]).json()
            for newPurchase in upList:
                    new = True
                    for purchase in purchaseList:
                        if(purchase[6] == str(newPurchase['_id'])):
                            #Not a new purchase
                            new = False
                    if(new):
                        db.tabulatePurchase(newPurchase, True)
                        print("New Purchase: ", newPurchase['_id'])
        #Handle Payouts
        print("Checking for incomplete payouts...")
        #See if there are any pending payouts and execute them
        payoutList = db.getPendingPayouts()
        for payout in payoutList:
            r = co_api.createPurchase(payout[2],
                                      payout[1],
                                      payout[3])
            if(int(r.json()['code']) == 201):
                db.completePayout(r.json()['objectCreated'], payout[0])
            else:
                print("Payout could not be completed.")
        
        time.sleep(3)

mainloop()
