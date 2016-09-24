import requests
import json

apiKey = 'e20498f24d98edbea7cb726685b02566'

#create customer
def createCustomer():
    customerData = {'first_name':'John',
                    'last_name':'Bonaguro',
                    'address':{
                        'street_number':'792',
                        'street_name':'Techwood Dr NW',
                        'city':'Atlanta',
                        'state':'GA',
                        'zip':'60514'
                        }
                    }
    r = requests.post('http://api.reimaginebanking.com/customers?key='+apiKey,
                      data = customerData)
    print(r.code);

createCustomer()
