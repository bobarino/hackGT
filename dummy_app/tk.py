import sys
import requests
import datetime
import json

if sys.version_info.major < 3:
    import Tkinter as tkinter
else:
    import tkinter

apiKey = 'e20498f24d98edbea7cb726685b02566'
accountID = '57e624c6dbd83557146123b9'
merchantID = '57e62a1cdbd83557146123bd'

app = tkinter.Tk()
app.title("SPEND MONEY")
amount = tkinter.StringVar()
accountNum = tkinter.StringVar()

f = tkinter.Frame(app)
sf2 = tkinter.Frame(f)
sf3 = tkinter.Frame(f)

_amount = tkinter.Entry(sf2, justify=tkinter.CENTER, textvariable=amount)
_accountNum = tkinter.Entry(sf3, justify=tkinter.CENTER, textvariable=accountNum)

def submitRequest():
    amt = float(amount.get())
    account_id = accountNum.get()
    
    now = datetime.datetime.now()
    purchaseData = {
                    'merchant_id':merchantID,
                    'medium':'balance',
                    'purchase_date':str(now),
                    'amount':amt,
                    'description':'Payout',
                    }
    r = requests.post('http://api.reimaginebanking.com/accounts/'+account_id
                          +'/purchases?key='+apiKey,
                      data = json.dumps(purchaseData),
                      headers = {'content-type':'application/json'})
    print(r.text)


img = []
def buildapp():
    f.pack()
    sf = tkinter.Frame(f)
    img = tkinter.PhotoImage(file="logo.gif")
    banner = tkinter.Label(sf, image=img)
    banner.image = img
    banner.pack()
    sf.pack(padx=15, pady=15)
    title = tkinter.Label(f, text="WELCOME TO SPENDBUCKS COFFEE")
    title.pack(padx=15, pady=15)

    subtitle = tkinter.Label(f, text="Please Enter your Total and Bank Account ID:")
    subtitle.pack(padx=15, pady=15)
    
    sf2.pack(padx=15, pady=15)
    ds = tkinter.Label(sf2, text="$")
    ds.pack(side=tkinter.LEFT)
    _amount.pack()
    
    sf3.pack(padx=15, pady=15)
    ns = tkinter.Label(sf3, text="#")
    ns.pack(side=tkinter.LEFT)
    _accountNum.pack()
    submit = tkinter.Button(f, text="Submit", command=submitRequest)
    submit.pack(expand=True, padx=15, pady=15)
    return app;

app = buildapp()
app.mainloop()

#float(s.get())
