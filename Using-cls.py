class student:
    
    stu="Harleen"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    @classmethod     #decorator to specify it as class method, now no need to pass class as an argument, 
    #use @staticmethod for no self/cls just simple static function execution
    def displayname(cls):
        print("My name is",cls.stu)

student.displayname()