class dost1:
    pen="parker"
class dost2(dost1):
    pencil="nataraj"
    def use(self):
        print("pen name =",self.pen)
        print("pencil name =",self.pencil)

d2=dost2()
d2.use()