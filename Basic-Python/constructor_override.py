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
      super(Second, self).output()  #solution to overriding of constructor

s=Second(600,600)
s.output()