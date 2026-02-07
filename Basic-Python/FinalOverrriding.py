from typing import final

class Raman:
    @final
    def use(self):
        print("Calling Raman Class")

class Seema(Raman):
    def use(self):  # Error: Method "use" cannot override final method defined in class "Raman" 
        print("Calling Seema Class")

S=Seema()
S.use()