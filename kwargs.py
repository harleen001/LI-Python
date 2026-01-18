#keyword variable arguments
def person(name,*data):
    print(name)
    print(data)

person("harleen",12,"mumbai",True)
# but we dont know what is type of data being passed so we use **data and use keywords

def keyperson(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

keyperson("harleen",age=12,homecity="mumbai",passed=True)