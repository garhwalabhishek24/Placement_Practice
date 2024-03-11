class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hi",self.name)
        print("mark",self.marks)
        
    def Garde(self):
        if self.marks>=60:
            print("A+") 
        elif self.marks>=50:
            print("B")
        elif self.marks>=35:
            print("C")
        else:
            print("Failed")
name=input("enter your name") 
marks=int(input("enter your marks"))           
s=Student(name,marks) 
s.Garde()
s.display()           
            
                             