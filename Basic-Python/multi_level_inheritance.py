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
  def use(self):
    print("Pen Name =",self.pen)
    print("Pencil Name =",self.pencil)
    print("Eraser Name=",self.eraser)

H=Harleen()
H.use()