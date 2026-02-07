class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
    def normalmethod(self):
        print("Student Name:",self.name)
        print("Student Rollno:",self.rollno)
    def __del__(self):
        print("Destructor Calling...")


obj = Student("Hari",1)
obj.normalmethod()

objj = Student("Sachin",2)
objj.normalmethod()

