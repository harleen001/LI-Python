class student:
    
    stu="Harleen"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def displayname(cls):
        print("My name is",cls.stu)

student.displayname(student)