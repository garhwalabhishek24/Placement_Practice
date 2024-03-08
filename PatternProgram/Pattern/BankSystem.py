import sys

class Bank:
    '''make bank with abhishek gadhwal'''
    bankname="ansh@bank"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance = self.balance+amount
        print("After Deposite amount",self.balance)

    def withdral(self,amount):
        if amount >self.balance:
            print("insufficient balance")
            sys.exit()
        self.balance = self.balance -amount
        print("After withdral yours balance",self.balance)
    def checkbalance(self):
        self.balance =print("your balance",self.balance)
        
print("Welcome to",Bank.bankname) 
name =input("enter your name  ")
b=Bank(name)
while True:
    print(' d-Deposite\n w-withdral\n c-checkbalance\n e-exit')
    option=input("choose your option")
    if option.lower()=="d":
        amount=float(input("Enter Amount to Deposit"))
        b.deposit(amount)
    if option.lower()=="w":
        amount=float(input("Enter Amount To Withdral"))
        b.withdral(amount)
    if option.lower()=="c":
        b.checkbalance()  
        
    if option=="e":         
        print("Thanks For Banking")
        sys.exit() 
    else:
        print("choose Valid Options")    
           
        
        
             
        
        









       
        
        
        
        
            
        
        
        
    
    
            
        
    