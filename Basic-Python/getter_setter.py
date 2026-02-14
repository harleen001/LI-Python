class First:
    def __init__(self,Dineshval):
        self.Dineshval=Dineshval

    @property
    def Meenuval(self):
        return self.__val
    @Meenuval.setter
    def Meenuval(self,Dineshval):
            self.__val=Dineshval
    @Meenuval.deleter
    def Meenuhval(self):
            del self.Dineshval


f=First(10)
f.Meenuval=220
print(f.Dineshval)
print(f.Meenuval)
