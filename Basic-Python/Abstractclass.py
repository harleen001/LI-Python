from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("Laptop is running")
l1=Laptop()
l1.process()
#com=Computer()
#com.process()