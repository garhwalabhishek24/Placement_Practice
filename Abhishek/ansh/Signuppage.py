from  tkinter import *
from  tkinter import messagebox
class Signup:
    def __init__(self,root):
        self.root = root
        self.root.title("singup System")
        self.root.geometry("1199x600+100+50") 
        
    #login frame
        Frame_login  = Frame(self.root , bg = "white")
        Frame_login.place(x=330 ,y = 150,width =500,height = 400)
        
    
    #Tittle 
        title = Label(Frame_login ,text="Signup Page",font = ("impact",35,"bold"),fg="#6162FF").place(x=90,y=30)    
        
    # for username
        lable_username = Label(Frame_login ,text="Username",font = ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        self.username = Entry(Frame_login ,font = ("Goudy old style",15,"bold"),bg="#E7E6E6")
        self.username.place(x=90,y=170,width = 320,height = 35)
    #for userpassword     
        lable_password = Label(Frame_login ,text="Password",font = ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
        self.password = Entry(Frame_login ,font = ("Goudy old style",15,"bold"),bg="#E7E6E6")
        self.password.place(x=90,y=240,width = 320,height = 35)
    # confirm password
        lable_confirmpassword = Label(Frame_login ,text="Confirm Password",font = ("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=275)
        self.confirmpassword = Entry(Frame_login ,font = ("Goudy old style",15,"bold"),bg="#E7E6E6")
        self.confirmpassword .place(x=90,y=300,width = 320,height = 35)
        
    # forgetpassword
    
        submitbutton = Button(Frame_login,command=self.check_function,text="Login",font = ("Goudy old style",15),bg="#6162FF",fg="white").place(x=90,y=350,width=180,height=40)
        
    def check_function(self):
        if self.username.get()=="" and self.password.get()=="" and self.confirmpassword.get()=="":
                messagebox.showerror("Error", "All fileds are required ",parent = self.root )
        elif self.password.get()=="":
            messagebox.showerror("Error", "please filled password",parent = self.root) 
        elif self.username.get()=="":
            messagebox.showerror("Error", "please filled username",parent = self.root)
        elif self.confirmpassword.get()=="":
            messagebox.showerror("Error", "please filled confrim password",parent = self.root)                 
        elif self.password.get()!= self.confirmpassword.get() :
                messagebox.showerror("Error", "Invalid password not match ",parent = self.root )
        else:
                messagebox.showinfo("Welcome", f"Welcome  {self.username.get()}")   
                 
    
root = Tk()
obj = Signup(root)
root.mainloop()
