class student():

    def __init__(self,name,rollno):
        self.__h_name=name
        self.__h_rollno=rollno

    @property
    def name(self):
        return self.h_name
    def rollno(self):
        return self.h_rollno

    @name.setter
    def name(self,name):
        self.h_name=name
    def rollno(self,rollno):
        self.h_rollno=rollno
#encapsulation in python
s=student("harleen","1")
s.name="Har"
s.rollno="12"
print(s.name)
print(s.rollno)
