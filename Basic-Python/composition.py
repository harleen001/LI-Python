class dost1:
    pen="parker"
class dost2:
    pencil="nataraj"
    def use(self):
        d1=dost1()
        print("pen name =",d1.pen)
        print("pencil name =",self.pencil)

d2=dost2()
d2.use()