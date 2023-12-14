from tkinter import*
win=Tk()
win.geometry('1920x1080')

def first():
    f=Frame(win)
    f.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Please Insert Your Card for ATM Service",font=("Rockwell",20))
    l.place(x=400,y=100)

    l1=Label(win,text="Welcome",font=("Rockwell",40))
    l1.place(x=530,y=150)

    l2=Label(win,text="To",font=("Rockwell",40))
    l2.place(x=610,y=230)

    l3=Label(win,text="Banking Services",font=("Rockwell",40))
    l3.place(x=450,y=300)

    b=Button(win,text="Inserted",bg="black",fg="light blue",command=second)
    b.place(x=750,y=550,width=100,height=50)

def second():
    f1=Frame(win)
    f1.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=460,y=50)

    l1=Label(win,text="Select your transaction",font=("Rockwell",15))
    l1.place(x=550,y=120)

    b=Button(win,text="Cash \nDeposit",bg="black",fg="light blue")
    b.place(x=300,y=180,width=150,height=50)

    b1=Button(win,text="Cash\nWithdrawl",bg="black",fg="light blue",command=cash)
    b1.place(x=900,y=180,width=150,height=50)

    b2=Button(win,text="Transfers &\nPayments",bg="black",fg="light blue")
    b2.place(x=300,y=280,width=150,height=50)

    b3=Button(win,text="Balance\nEnquiry",bg="black",fg="light blue",command=balance)
    b3.place(x=900,y=280,width=150,height=50)

    b4=Button(win,text="PIN Change",bg="black",fg="light blue",command=pin)
    b4.place(x=300,y=380,width=150,height=50)

    b5=Button(win,text="Set Prefrences",bg="black",fg="light blue")
    b5.place(x=900,y=380,width=150,height=50)

    l2=Label(win,text="Press",font=("Rockwell",15))
    l2.place(x=500,y=500)

    b6=Button(win,text="CANCEL",bg="black",fg="light blue",command=first)
    b6.place(x=560,y=500,width=50,height=30)

    l3=Label(win,text="to Exit",font=("Rockwell",15))
    l3.place(x=620,y=500)

def cash():
    f2=Frame(win)
    f2.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Cash Withdrawl",font=("Rockwell",15))
    l1.place(x=540,y=150)

    l2=Label(win,text="Select the Account type",font=("Rockwell",15))
    l2.place(x=510,y=220)

    b=Button(win,text="Saving Account",bg="black",fg="light blue")
    b.place(x=720,y=270,width=150,height=50)

    b=Button(win,text="Current Account",bg="black",fg="light blue",command=current)
    b.place(x=720,y=360,width=150,height=50)

def current():
    f3=Frame(win)
    f3.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Cash Withdrawl",font=("Rockwell",15))
    l1.place(x=540,y=150)

    l2=Label(win,text="Enter Amount",font=("Rockwell",20))
    l2.place(x=530,y=230)   

    e=Entry(win,font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=530,y=280,width=180,height=50)

    b=Button(win,text="Proceed",bg="black",fg="light blue",command=proceed)
    b.place(x=700,y=550,width=100,height=50) 

def proceed():
    f4=Frame(win)
    f4.place(x=0,y=0,width=1920,height=1080)
        
    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l=Label(win,text="Enter Password",font=("Rockwell",15))
    l.place(x=520,y=230)
    
    e=Entry(win,show="*",font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=520,y=280,width=150,height=50)

    b=Button(win,text="Confirm",bg="black",fg="light blue",command=confirm)
    b.place(x=700,y=550,width=100,height=50)

def confirm():
    f5=Frame(win)
    f5.place(x=0,y=0,width=1920,height=1080) 

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Your transaction is being processing.......",font=("Rockwell",15))
    l1.place(x=400,y=190)

    b=Button(win,text="OK",bg="black",fg="light blue",command=ok)
    b.place(x=550,y=450,width=100,height=50)


def ok():
    f5=Frame(win)
    f5.place(x=0,y=0,width=1920,height=1080) 

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Congrats!!!!",font=("Rockwell",20))
    l1.place(x=500,y=190)

    l2=Label(win,text="Your transaction is completed",font=("Rockwell",15))
    l2.place(x=430,y=230)

    b=Button(win,text="Exit",bg="black",fg="light blue",command=first)
    b.place(x=520,y=280,width=100,height=30)

def pin():
    f6=Frame(win)
    f6.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    b=Button(win,text="Reset Password",bg="black",fg="light blue",font=("Rockwell",15),command=reset)
    b.place(x=500,y=180,width=200,height=50)

def reset():
    f7=Frame(win)
    f7.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Enter the Mobile number linked with the account",font=("Rockwell",15))
    l1.place(x=370,y=200)

    e=Entry(win,font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=470,y=280,width=250,height=50)

    b=Button(win,text="Next",bg="black",fg="light blue",font=("Rockwell",15),command=next)
    b.place(x=650,y=530,width=100,height=30)

def next():
    f8=Frame(win)
    f8.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Enter OTP sent on your mobile",font=("Rockwell",15))
    l1.place(x=430,y=200)

    e=Entry(win,font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=500,y=280,width=130,height=50)

    b=Button(win,text="Next",bg="black",fg="light blue",font=("Rockwell",15),command=third)
    b.place(x=650,y=500,width=200,height=30)

    b1=Button(win,text="Resend OTP",bg="black",fg="light blue",font=("Rockwell",15))
    b1.place(x=650,y=540,width=200,height=30)

def third():
    f9=Frame(win)
    f9.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Enter New Password",font=("Rockwell",15))
    l1.place(x=350,y=250)

    e=Entry(win,font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=350,y=290,width=200,height=30)

    l2=Label(win,text="Confirm Password",font=("Rockwell",15))
    l2.place(x=350,y=350)

    e=Entry(win,font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=350,y=390,width=200,height=30)

    b=Button(win,text="Next",bg="black",fg="light blue",font=("Rockwell",15),command=four)
    b.place(x=500,y=500,width=100,height=30)

def four():
    f10=Frame(win)
    f10.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Your password is updated Sucessfully",font=("Rockwell",15))
    l1.place(x=410,y=230)

    b=Button(win,text="Exit",bg="black",fg="light blue",font=("Rockwell",15),command=first)
    b.place(x=540,y=500,width=100,height=30)

def balance():
    f11=Frame(win)
    f11.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="To check your balnace",font=("Rockwell",15))
    l1.place(x=500,y=230)

    l1=Label(win,text="press OK",font=("Rockwell",15))
    l1.place(x=540,y=270)

    b=Button(win,text="OK",bg="black",fg="light blue",font=("Rockwell",15),command=five)
    b.place(x=540,y=500,width=100,height=30)

def five():
    f11=Frame(win)
    f11.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Enter Password",font=("Rockwell",15))
    l1.place(x=500,y=200)

    e=Entry(win,show="*",font=("Rockwell",15),bg="black",fg="light blue")
    e.place(x=500,y=240,width=150,height=30)

    b=Button(win,text="Confirm",bg="black",fg="light blue",font=("Rockwell",15),command=six)
    b.place(x=700,y=500,width=80,height=30)

def six():
    f12=Frame(win)
    f12.place(x=0,y=0,width=1920,height=1080)

    l=Label(win,text="Banking Desktop App",font=("Rockwell",30))
    l.place(x=400,y=50)

    l1=Label(win,text="Your Net.Amount is:",font=("Rockwell",15))
    l1.place(x=500,y=200)

    b=Button(win,text="Exit",bg="black",fg="light blue",font=("Rockwell",15),command=second)
    b.place(x=540,y=500,width=100,height=30)


first()
win.mainloop()
    