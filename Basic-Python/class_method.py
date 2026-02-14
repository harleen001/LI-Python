class rectangle:
    def __init__(self,length,breadth):
            self.length = length
            self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    @classmethod
    def square(cls,side):
        return cls(side,side)
s= rectangle.square(10)
print("area = ",s.area())