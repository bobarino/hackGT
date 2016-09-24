import requests
import json
import datetime

apiKey = 'e20498f24d98edbea7cb726685b02566'
customerID = '57e62291dbd83557146123b6'
accountID = '57e624c6dbd83557146123b9'
merchantID = '57e62a1cdbd83557146123bd'

r = {}

#create customer
def createCustomer():
    address = {
                'street_number':'792',
                'street_name':'Techwood Dr NW',
                'city':'Atlanta',
                'state':'GA',
                'zip':'30313'
                }
    customerData = {'first_name':'John',
                    'last_name':'Bonaguro',
                    'address': address
                    }
    print(customerData)
    r = requests.post('http://api.reimaginebanking.com/customers?key='+apiKey,
                      data = json.dumps(customerData),
                      headers={'content-type':'application/json'})
    print(r.text);


#createCustomer()

def createAccount():
    accountData = {
                    'type':'Checking',
                    'nickname':'Checking',
                    'rewards': 0,
                    'balance': 100,
                    }
    print(accountData)
    r = requests.post('http://api.reimaginebanking.com/customers/'+customerID+'/accounts?key='+apiKey,
                      data = json.dumps(accountData),
                      headers = {'content-type':'application/json'})
    print(r.text)

#createAccount()

def createMerchant():
    merchantData = {
                    'name':'TestCharity',
                    'category':['Charity'],
                    }
    print(merchantData)
    r = requests.post('http://api.reimaginebanking.com/merchants?key='+apiKey,
                      data = json.dumps(merchantData),
                      headers = {'content-type':'application/json'})
    print(r.text)

#createMerchant()

def makePurchase():
    purchaseAmount = 5.00
    purchaseData = {
                    'merchant_id':merchantID,
                    'medium':'balance',
                    'purchase_date':str(datetime.datetime.now()),
                    'amount':purchaseAmount,
                    'description':'Test payment',
                    }
    print(purchaseData)
    r = requests.post('http://api.reimaginebanking.com/accounts/'+accountID
                          +'/purchases?key='+apiKey,
                      data = json.dumps(purchaseData),
                      headers = {'content-type':'application/json'})
    print(r.text)

#makePurchase()

def getPurchase():
    r = requests.get('http://api.reimaginebanking.com/accounts/'+accountID
                          +'/purchases?key='+apiKey)
    print(r.text)

def getAccount():
    r = requests.get('http://api.reimaginebanking.com/accounts/'+accountID
                         +'?key='+apiKey)
    print(r.text)

def getCustomer():
    r = requests.get('http://api.reimaginebanking.com/customers/'+customerID
                         +'?key='+apiKey)
    print(r.text)
    
def getMerchant():
    r = requests.get('http://api.reimaginebanking.com/merchants/'+merchantID
                         +'?key='+apiKey)
    print(r.text)
