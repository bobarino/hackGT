import sys

if sys.version_info.major < 3:
    import Tkinter as tkinter
else:
    import tkinter

def submitRequest():
    pass

img = []
def buildapp():
    app = tkinter.Tk()
    f = tkinter.Frame(app)
    f.pack()
    sf = tkinter.Frame(f)
    img = tkinter.PhotoImage(file="logo.gif")
    banner = tkinter.Label(sf, image=img)
    banner.image = img
    banner.pack()
    sf.pack(padx=15, pady=15)
    label = tkinter.Label(f, text="WELCOME TO E-CORP")
    label.pack()
    s = tkinter.Entry(f, justify=tkinter.CENTER)
    s.pack()
    sf2 = tkinter.Frame(f)
    sf2.pack()
    #label = tkinter.Label(sf2, text="DIRECTION")
    #label.pack()
    submit = tkinter.Button(sf2, text="Submit")#, command=submitRequest)
    submit.pack(expand=True)
    return app;

app = buildapp()
app.mainloop()

#float(s.get())
