from Pratice.Test import  empolyee
class employeeinformation(empolyee):
    def __init__(self,ename, elastname,eadress,esal,ecar,insorance):
        super().__init__(ename, elastname,eadress,esal)
        self.ecar=ecar
        self.insorance=insorance
        
    def display(self):
        empolyee.display(self) 
        print("the employee having car",self.ecar)
        print("the employee insorance",self.insorance)
        
        
e=employeeinformation("ansh","gadhwal","burhanpur",12000,"yes","yes")
e1=employeeinformation("abhishek","shinde","khandwa",123000,"no","no")
e1.display()
        
    