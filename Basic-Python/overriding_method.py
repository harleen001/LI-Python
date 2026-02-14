
class Dost0:
    def use(self):
        print("Hello Dost0 is calling.....")



class Dost1:
    def use(self):
        super().use()
        print("Hello Dost1 is calling.....")
class Dost2:
    def use(self):
        super().use()
        print("Hello Dost2 is calling.....")

class Dost3(Dost2,Dost1,Dost0):
    def use(self):
        super().use()
        print("Hello Dost3 is calling.....")


d3=Dost3()
d3.use()