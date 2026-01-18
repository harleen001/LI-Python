def update(x):
    x+=2
    print(x)


update(5)
#function having an argument will be pass by value,same id but when value passed, we dont use any of them basically new memory created


def student(name,age): 
    print(f"{name} is {age} years old")

student("kartik",22) #positional argumentsn
student(age=22,name="harleen") #keyword arguments
