from OOPs import Student
class student(Student.test):
    def __init__(self,name,adress,department,studentId):
        super().__init__(name,adress)
        self.department=department
        self.studentId=studentId
        
    def display(self):
        super().display()
        print("the student department is",self.department)
        print("the student Id is",self.studentId)
        
s=student("ansh","lalbagh","mca",1)
s.display()        
        

