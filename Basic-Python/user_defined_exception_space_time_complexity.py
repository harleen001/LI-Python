class MRException(Exception):
  def __init__(self,field):
    self.field=field
class MAException(Exception):
    def __init__(self,age):
     self.age=age
class MMException(Exception):
    def __init__(self,marks):
     self.marks=marks

try:
  name=(input("Enter your name ="))
  rollno=(input("Enter your rollno ="))
  age=(input("Enter your age ="))
  marks=(input("Enter your marks ="))
  if len(name)>0:
    if len(rollno)>0:
      if len(age)>0:
        if len(marks)>0:
          print("Data is entered")
  else:
       raise MRException("Field is empty")

  if (int(age)>18 and int(age)<60):
     print("Entered age is valid")
  else:
       raise MAException("Entered age is not valid")

  if (int(marks)>0 and int(marks)<100):
       print("Entered marks are valid")
  else:
       raise MMException("Entered marks are not valid")

except MRException as R:
    print(R)
except MAException as A:
     print(A)
except MMException as M:
     print(M)