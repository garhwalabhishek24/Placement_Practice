from  tkinter import *
from  tkinter import messagebox
from setuptools.command.setopt import config_file
from msilib.schema import RadioButton

class Createaccount:
    def __init__(self,root):
        self.root = root
        self.root.title = "Create Account "
        self.root.geometry("1300x800+200+100")
        
        Acountpanel  = Frame(self.root , bg = "white")
        Acountpanel.place(x=300 ,y = 30,width =500,height = 600)
    # for username:    
        title  = Label(  Acountpanel ,text="Create New Account",font = ("impact",30,"bold"),fg="#6162FF").place(x=50,y=30)
        lable_username = Label(Acountpanel ,text="User Name",font = ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=40,y=100)
        self.username= Entry(Acountpanel,font = ("Goudy old style",10,"bold"),bg="#E7E6E6")
        self.username.place(x=40,y=140,width = 340,height = 35)
    # for email 
        lable_gmail  =Label(Acountpanel,text= "Gmail Id ",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=40,y=220) 
        self.gmail= Entry(Acountpanel,font= ("Goudy old style",10,"bold"),bg="#E7E6E6") 
        self.gmail.place(x=40,y=260,width=340,height=35) 
        
    # for Mobile number    
        lable_mobile = Label(Acountpanel,text ="Mobile Number",font= ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=40,y=300)
        self.mobile = Entry(Acountpanel,font=("Goudy old style",10,"bold"),bg="#E7E6E6")
        self.mobile.place(x=40,y=340,width =340,height=35)
    # for password 
        lable_password = Label(Acountpanel,text ="Password",font= ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=40,y=420)
        self.password = Entry(Acountpanel,font=("Goudy old style",10,"bold"),bg="#E7E6E6")
        self.password.place(x=40,y=460,width = 340,height=35) 
        
        lable_password = Label(Acountpanel,text ="Select State",font= ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=40,y=180)
    # for Gender    
        option = StringVar()
        state=["MadhyaPradesh","UtterPradesh","maharasthra","Punjab","Tamilnadu","Gujarat","Rajasthan"]
        option.set(" Select your state  ")
        dropdown = OptionMenu(root,option,*state).pack(padx=150,pady=220)
        submitbutton = Button(Acountpanel,text="Login",font = ("Goudy old style",15),bg="#6162FF",fg="white").place(x=90,y=540,width=180,height=40)

        
    
    
        
    
    
    
root = Tk()
obj = Createaccount(root)
root.mainloop()
  