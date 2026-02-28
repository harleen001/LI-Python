from threading import *

class Hello:
    def run(Thread):    #changing self to thread 
        for i in range(5):
            print("Hello")

class Hi:
    def run(Thread):
        for i in range(5):
            print("Hi")

t1=Hello()
t2=Hi()

t1.run()
t2.run()

#hello taking 5 seconds and hi taking 5 seconds, all of total 10 seconds but i want them to run simulatenously