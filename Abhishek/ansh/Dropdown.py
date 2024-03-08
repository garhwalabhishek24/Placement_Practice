from  tkinter import *
from msilib.schema import RadioButton
from  tkinter import messagebox
from setuptools.command.setopt import config_file

class ansh:
    
    def __init__(self,root):
        self.root = root
        self.root.title = "Dropdown "
        self.root.geometry("1300x800+200+100")
        
        Dropdown  = Frame(self.root , bg = "red")
        Dropdown.place(x=300 ,y = 300,width =500,height = 600)
        option = StringVar()
        state=["MadhyaPradesh","UtterPradesh","maharasthra","Punjab","Tamilnadu","Gujarat","Rajasthan"]
        option.set(" Select your state  ")
        dropdown = OptionMenu(root,option,*state).pack(padx=150,pady=220)
        submitbutton = Button(Dropdown,text="Login",font = ("Goudy old style",15),bg="#6162FF",fg="white").place(x=90,y=540,width=180,height=40)


root = Tk()
root.mainloop()