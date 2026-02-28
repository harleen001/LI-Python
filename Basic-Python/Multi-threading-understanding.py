from threading import *
from time import sleep
class Hello(Thread):
    def run(self):    #changing self to thread 
        for i in range(5):
            print("Hello")
            sleep(0.5)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)

t1=Hello()
t2=Hi()

#t1.run()
#t2.run()

t1.start()
t2.start()


#waits for both to finish
t1.join()
t2.join()
print("Completed")

#hello taking 5 seconds and hi taking 5 seconds, all of total 10 seconds but i want them to run simulatenously

#even making class to threads wont run this simultaneous  so instead of run() use start()