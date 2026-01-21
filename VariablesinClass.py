class car:
    wheels=4
    def __init__(self):
        self.mil=8
        self.company="BMW"

c1=car()
c2=car()
c1.mil=10  #INSTANCE Variable different for different values
#instance variables inside __init__ and in class are static class variables
print(c1.mil,c1.company,c1.wheels)
print(c2.mil,c2.company,c2.wheels)