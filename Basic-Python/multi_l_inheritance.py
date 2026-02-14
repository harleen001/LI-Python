class dost1:
    pen="parker"
class dost2(dost1):
    pencil="nataraj"
class dost3(dost2):
    eraser="sensil"
    def use(self):
        print("pen name =",self.pen)
        print("pencil name =",self.pencil)
        print("eraser name =", self.eraser)

d3=dost3()
d3.use()