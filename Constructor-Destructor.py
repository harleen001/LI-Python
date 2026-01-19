class Student:
    def __init__(self):
        print("Constructor Calling...")
  
    def normalmethod(self):
        print("Normal Method Calling...")
  
    def __del__(self):
        print("Destructor Calling...")


obj = Student()
obj.normalmethod()

objj = Student()
objj.normalmethod()

