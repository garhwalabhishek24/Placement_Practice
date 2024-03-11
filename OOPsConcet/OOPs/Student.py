class test:
    def __init__(self,name,adress):
        self.name=name
        self.adress =adress
       
    def ansh(self):
        print("the student name is",self.name)
        print("the student adress is",self.adress)
        
class emp(test):  
         
    def __init__(self,name,adress,department):
        super().__init__(name,adress) 
        self.department=department
        
    def ansh(self):
        test.ansh(self)
        print("the student department is",self.department) 
        
e=emp("ansh",'lalbagh',"mca")
e.ansh()               