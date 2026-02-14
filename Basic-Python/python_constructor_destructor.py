class student:
  
  def __init__(self):
    print("hello dost")
    print("i am constructor")

  def output(self):
    print("normal function calling")

  def __del__(self):
    print("destructor calling")

s1=student()
s1.output()
s2=student()
s2.output()