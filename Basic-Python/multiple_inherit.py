class Dost1:
    pen='parker'
class Dost2():
    pencil="Natraj"
class Dost3(Dost1,Dost2):
    eraser="sensil"
    def use(self):
        print("pen name=",self.pen)
        print("pencil name=", self.pencil)
        print("eraser name=", self.eraser)
d3=Dost3()
d3.use()