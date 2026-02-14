class Kartik:
  pen='parker'

class Ansh:
  pencil='natraj'
  def use(self):
    K=Kartik()
    print("Pen Name =",K.pen)
    print("Pencil Name =",self.pencil)

A=Ansh()
A.use()

#Single Level Inheritance
class Kartik: #super class
  pen='parker'

class Ansh(Kartik): #ansh sub class
  pencil='natraj'
  def use(self):
    
    print("Pen Name =",self.pen)
    print("Pencil Name =",self.pencil)

A=Ansh()
A.use()

#MultiLevel Level Inheritance
class Kartik: #super class
  pen='parker'

class Ansh(Kartik): #ansh sub class acts as super class for Harleen
  pencil='natraj'
class Harleen(Ansh):
  eraser="Sensil"
class saini(Harleen):
  scale="apsara"

  def use(self):
    print("Pen Name =",self.pen)
    print("Pencil Name =",self.pencil)
    print("Eraser Name=",self.eraser)
    print("scale name=",self.scale)

S=saini()
S.use()

student={'name':'Raj','rollno':3,'english':50,'maths':60,'science':70,'punjabi':80,'hindi':90}
sum=0
for i in range(2,len(student)):
  value_at_index = list(student.values())[i]
  sum+=value_at_index
print("Total marks =",sum)
print("percentage =",sum//5)
student['total']=sum
student['percentage']=sum//5
print(student)

#METHOD OVERRIDING
class Dost1:
  def output(self):
    print("Hello I am Dost1")

class Dost2(Dost1):
  def output(self):
    super().output()
    print("Hello I am Dost2")

d2=Dost2()
d2.output()

#CONSTRUCTOR OVERRIDING SOLUTION
class First:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def output(self):
        print("Class First:",(self.x+self.y))

class Second(First):
    def __init__(self,a,b):
        super(Second,self).__init__(20,30)
        self.a=a
        self.b=b
    def output(self):
      print("Class Second:", (self.a + self.b))
      super(Second,self).output()

s=Second(600,600)
s.output()